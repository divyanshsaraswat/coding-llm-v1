# Model Architecture Documentation

## Why Small Models?
We use a model with ≤ 200M parameters intentionally.
1.  **Iteration Speed:** We can train these on consumer GPUs (or even CPUs for very small models) in minutes/hours, allowing for rapid experimentation with learning rates and datasets.
2.  **Interpretability:** It is easier to debug and analyze the behavior of smaller networks.
3.  **Failure Analysis:** Small models fail more often and more obviously, making them perfect subjects for studying hallucinations and logic errors.

## The "Loss vs Correctness" Gap
A critical lesson: **Low Validation Loss does NOT mean Correct Code.**
*   **Loss** measures how well the model predicts the next token (syntax, keywords).
*   **Correctness** requires logical consistency, which statistical prediction often mimics but doesn't "understand."
*   A model can have near-perfect syntax (low loss) but hallucinate libraries that don't exist (0% correctness).
