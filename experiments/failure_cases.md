# Failure Case Log

## Objective
Document specific instances where the model generates incorrect, dangerous, or nonsensical code.

## Infinite Loops
*   **Prompt:** `while True:`
*   **Result:** `while True: +=spacesroddown n count_nums + total n return result = totalli):`
*   **Analysis:** The model recognizes `while True` starts a block, but immediately devolves into a bag-of-words. It does not understand loop termination conditions.

## Library Hallucinations
*   **Prompt:** `from sklearn.metrics import`
*   **Result:** `from s ⁇ learn.metrics import result[posum result fib if n * sy`
*   **Analysis:**
    1.  **Tokenizer Failure:** The character `k` in `sklearn` appears to be tokenized as `[UNK]` (⁇). This suggests our vocab size of 500 was *too small* to capture even all lowercase alphabet letters if they weren't in the top 500 tokens (which is surprising, but possible if `return`, `def`, spaces, and common bigrams took up all slots).
    2.  **Syntax salad:** It strings together `result`, `fib`, `if` without structure.

## Syntax Errors
*   **Prompt:** `def factorial(n):`
*   **Result:** `def factorial(n):): exp while fa>>):,ductctalind`
*   **Analysis:**
    *   **Echoing:** It repeats the colon `):):`.
    *   **Garbage generation:** `ductctalind` looks like a hallucinated variable blending "product" and "index"?
