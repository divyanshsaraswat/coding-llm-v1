# Coding LLM Education

## Project Intent
This project is an experimental, educational initiative designed to understand the inner workings of coding language models (LLMs). The goal is to build a small, Python-only causal language model from scratch to study how code is tokenized, how next-token prediction works, and importantly, where these models fail. This is a "glass box" approach to AI, prioritizing transparency and understanding over performance.

## Non-Goals
*   **Production Readiness:** This code is NOT intended for production use.
*   **Performance Optimization:** Efficiency is secondary to clarity.
*   **Large Scale:** We are restricted to small models (≤ 200M params) and small datasets.
*   **Deployment:** There is no deployment pipeline or infrastructure.

## Learning Outcomes
By exploring this project, we aim to:
1.  Visually inspect how source code is broken down into tokens.
2.  Understand the mechanics of autoregressive generation.
3.  Analyze specific failure modes and hallucinations in code generation.
4.  Critically evaluate the trust boundaries we should place around AI-generated code.

> [!WARNING]
> **Trust Warning:** Do NOT over-trust the output of this model or any LLM. These models are statistical predictors, not reasoning agents. They can and will generate syntactically correct but logically flawed or dangerous code. Always verify AI-generated code.
