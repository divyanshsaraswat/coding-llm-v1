# Hallucination Analysis

## Definition
A **hallucination** in coding is when the model generates code that is syntactically valid but refers to non-existent libraries, functions, or variables.

## Examples Observed

### 1. The "Wishful Thinking" Import
*   **Code:** `from utils import calculate_magic_number`
*   **Reality:** `utils.py` does not exist or has no such function.
*   **Cause:** The model saw similar imports in training data and "invented" one to solve the problem.

### 2. The Argument Shuffle
*   **Code:** `model.train(epochs=10, data=loader)`
*   **Reality:** `train()` function signature is actually `train(loader, epochs)`.
*   **Cause:** Statistical probability of argument names vs actual API enforcement.
