import regex
from lark import UnexpectedInput, Lark, UnexpectedCharacters, UnexpectedToken, UnexpectedEOF, UnexpectedInput
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

import numpy as np
from transformers import LogitsProcessor, AutoModelForCausalLM, AutoTokenizer, BeamSearchScorer, LogitsProcessorList, MaxLengthCriteria, StoppingCriteriaList
import torch
from dataclasses import dataclass
from typing import List, Optional, Union


@dataclass
class IntermediateParsingState: 
    active_terminal_names: List[str]
    active_terminal_patterns: List[regex.Regex]
    current_terminal_start_index: int

    def __str__(self) -> str:
        return f"({self.current_terminal_start_index}, {self.active_terminal_names})"
    
    def __repr__(self) -> str:
        return str(self)


class ParsingStepper():
    def __init__(self, parser: Lark, vocab, eos_token):
        self.parser: Lark = parser
        self.partial_token = ""
        self.vocab = vocab
        self.eos_token = eos_token
        self.regex_map = self._create_terminal_regexes()

    def _create_terminal_regexes(self):
        """
        Create a map from terminal names to regexes that match the terminal
        """
        terminal_regexes = {}
        for terminal in self.parser.terminals:
            if terminal.pattern:
                terminal_regexes[terminal.name] = regex.compile(terminal.pattern.to_regexp())
        terminal_regexes['$END'] = regex.compile(self.eos_token)
        return terminal_regexes

    def get_parsing_state(self, current_generation: str): 

        # Get the next parser tokens that would be valid to add to the input string according to the CFG
        next_parser_tokens, token_start_index = self._get_next_parser_tokens(current_generation)
        # Get the regexes for the next parser tokens
        next_patterns = [self.regex_map[terminal] for terminal in next_parser_tokens]
        
        return IntermediateParsingState(next_parser_tokens, next_patterns, token_start_index)
    
    def _get_next_parser_tokens(self, input_str):
        """
        Get the next tokens that would be valid to add to the input string
        :return: A list of tokens that would be valid to add to the input string, and the position in the input string where the next token would start
        """
        try:
            # Try parsing until error or end of input
            self.parser.parse(input_str)
        except UnexpectedInput as e:
            interactive = self.parser.parse_interactive(input_str)
            try: 
                # Get the set of tokens that would be valid next
                interactive.exhaust_lexer()
            except UnexpectedInput as ee: 
                # Now, this exception means that we have characters that do not match any of the terminals (yet). 
                # This means that we have a partial token.
                # Return the set of tokens that would be valid before that partial token 
                print("Second catch")
                return interactive.accepts(), ee.pos_in_stream
            # Return the token 
            return interactive.accepts(), e.pos_in_stream
 
        # If we get here, the input is complete
        return [], len(input_str)
