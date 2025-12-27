# Compiler vs. Model Comparison

## Objective
Compare the "fuzzy" probation of the model against the "strict" rules of the Python interpreter.

## Experiment
Take 100 generated samples. Run them through `python -m py_compile`.

## Results
*   **Syntax Errors:** X% (Model failed language rules)
*   **Runtime Errors:** Y% (Model failed logic/existence rules)
*   **Correct Execution:** Z%

## Insight
The compiler is the ultimate ground truth. The model is an approximation function. The gap between them is the "Trust Gap."
