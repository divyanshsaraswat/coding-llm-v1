# Tokenizer Documentation

## Why Tokenization Matters for Code
Tokenization is the critical first step in LLMs. For code, it is even more sensitive than natural language because:
1.  **Indentation:** Python relies on whitespace. If the tokenizer treats 4 spaces differently than a tab, the model must learn that.
2.  **Syntax:** Brackets `{}`, `[]`, `()` are syntactically rigid. Breaking them incorrectly ruins the structure.
3.  **Compound Words:** Function names like `calculate_mean_value` might be split into `calculate`, `_`, `mean`, `_`, `value` or `calculate_mean`, `_value`. This affects how the model perceives the API.

## What to Inspect Manually
When evaluating your tokenizer, specifically look for:
*   **Whitespace:** How are spaces and newlines represented? (e.g., ` ` vs `\n`).
*   **Keywords:** Are `def`, `class`, `import` single tokens?
*   **Operators:** Are `==`, `!=`, `>=` single tokens or split sequence?
