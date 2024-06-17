# FuncQA Experiments: Syntax error-free decoding for Math Equations

This repo shows two methods for syntax error-free decoding 

 - using a context-free grammar (defined with lark)
 - using a finite-state automtata that is evaluated directly on the GPU

It uses these approaches to improve the performance of the Zephyr 7B LLM on FuncQA, a math equation benchmark. This approach outperforms current state-of-the-art. 

It was developed as part of a seminar at [HPI](hpi.de). Here are additional resources 

 - [**Slides**](./docs/slides.pdf) outlining the basic idea
  - [**Report**](./docs/report.pdf) outlining the approach in-depth


 ## Literature

The methods implemented here are inspiered by the following two papers 

1. ToolDec: Syntax Error-Free and Generalizable Tool Use for LLMs via Finite-State Decoding [[arxiv]](https://arxiv.org/pdf/2310.07075.pdf)
2. ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings [[arxiv]](https://arxiv.org/abs/2305.11554)


