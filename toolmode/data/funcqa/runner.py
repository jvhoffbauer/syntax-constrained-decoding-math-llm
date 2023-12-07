import ast

from toolmode.data.funcqa.math_operators import (
    add_,
    choose_,
    divide_,
    gcd_,
    lcm_,
    ln_,
    log_,
    multiply_,
    permutate_,
    power_,
    remainder_,
    sqrt_,
    subtract_,
)

OPERATORS = {
    "add": add_,
    "subtract": subtract_,
    "multiply": multiply_,
    "divide": divide_,
    "power": power_,
    "sqrt": sqrt_,
    "log": log_,
    "ln": ln_,
    "choose": choose_,
    "permutate": permutate_,
    "gcd": gcd_,
    "lcm": lcm_,
    "remainder": remainder_,
}


def evaluate_toolcall(text: str):
    # Run the text as a Python function call with the operators imported
    # Use ast.literal_eval to prevent arbitrary code execution
    try:
        result = literal_eval_with_callables(text, OPERATORS)
    except Exception as e:
        result = None

    return result


def literal_eval_with_callables(node_or_string, safe_callables=None):
    if safe_callables is None:
        safe_callables = {}
    if isinstance(node_or_string, str):
        node_or_string = ast.parse(node_or_string, mode="eval")
    if isinstance(node_or_string, ast.Expression):
        node_or_string = node_or_string.body
    try:
        # Python 3.4 and up
        ast.NameConstant
        const_test = lambda n: isinstance(n, ast.NameConstant)
        const_extract = lambda n: n.value
    except AttributeError:
        # Everything before
        _const_names = {"None": None, "True": True, "False": False}
        const_test = lambda n: isinstance(n, ast.Name) and n.id in _const_names
        const_extract = lambda n: _const_names[n.id]

    def _convert(node):
        if isinstance(node, (ast.Str, ast.Bytes)):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Tuple):
            return tuple(map(_convert, node.elts))
        elif isinstance(node, ast.List):
            return list(map(_convert, node.elts))
        elif isinstance(node, ast.Dict):
            return dict((_convert(k), _convert(v)) for k, v in zip(node.keys, node.values))
        elif const_test(node):
            return const_extract(node)
        elif (
            isinstance(node, ast.UnaryOp)
            and isinstance(node.op, (ast.UAdd, ast.USub))
            and isinstance(node.operand, (ast.Num, ast.UnaryOp, ast.BinOp))
        ):
            operand = _convert(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            else:
                return -operand
        elif (
            isinstance(node, ast.BinOp)
            and isinstance(node.op, (ast.Add, ast.Sub))
            and isinstance(node.right, (ast.Num, ast.UnaryOp, ast.BinOp))
            and isinstance(node.right.n, complex)
            and isinstance(node.left, (ast.Num, ast.UnaryOp, ast.BinOp))
        ):
            left = _convert(node.left)
            right = _convert(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            else:
                return left - right
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in safe_callables:
            return safe_callables[node.func.id](
                *[_convert(n) for n in node.args], **{kw.arg: _convert(kw.value) for kw in node.keywords}
            )
        raise ValueError("malformed string")

    return _convert(node_or_string)


def main():
    print(evaluate_toolcall("1 + 2"))
    print(evaluate_toolcall("import os; os.system('sleep 2')"))
    print(evaluate_toolcall("add(1, 2)"))
    print(evaluate_toolcall("subtract(1, 2)"))


if __name__ == "__main__":
    main()
