# Final Reflection

## What the Model Does Well
*   **Syntactic Mimicry:** It learned to produce Python-like keywords (`def`, `return`, `if`, `while`) and indentation structures very quickly (within 5 epochs).
*   **Memorization (Partial):** After heavy fine-tuning (50 epochs), it began to memorize parts of the training data, though it struggled to recall them perfectly due to tokenizer limits.
*   **Format Adherence:** It attempted to follow the `Instruction: ... Output:` format, even if the content was garbled.

## Where It Fails
*   **The "Vocabulary Blindness":** This was the most critical failure. With a vocabulary of only 500 tokens, the model treated common letters (like 'k' in `sklearn` or 'I' in `Instruction`) as `[UNK]` (unknown). This made it effectively "blind" to critical prompts.
*   **Logic & Reasoning:** It generated "syntax salad"—code that looks like code from a distance but makes no logical sense (e.g., `while True: +=spaces`).
*   **Hallucination:** It confidently invented library names and variable names that didn't exist in the context, purely based on statistical probability.

## Why Those Failures Happen
1.  **Tokenizer Bottleneck:** A model is only as intelligent as its tokenizer allows. If the tokenizer cannot represent the input, the model cannot learn it.
2.  **Next-Token Prediction != Understanding:** The model optimizes for minimizing the surprise of the *next* token. It does not optimize for "program correctness" or "logical flow."
3.  **Data Scarcity:** Learning a programming language from ~50 snippets is impossible for generalization. It requires millions of examples to learn the *rules* of syntax rather than just memorizing lines.

## When I Trust LLMs
*   **Boilerplate:** Generating standard structures I know well (e.g., "Create a React component").
*   **Brainstorming:** Getting a list of ideas or libraries to investigate.
*   **Transformations:** converting JSON to CSV, or formatting text (tasks where logic is shallow).

## When I Do NOT Trust LLMs
*   **Blind Execution:** I will never run LLM-generated code without reading it line-by-line.
*   **Obscure Libraries:** If I don't know the library, I assume the LLM might be hallucinating function names.
*   **Security Critical Logic:** Auth flows, cryptography, or data handling. The model optimizes for "likely" code, which often includes "common insecure" code.
