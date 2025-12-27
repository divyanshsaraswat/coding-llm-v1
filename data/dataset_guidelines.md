# Dataset Guidelines

## Purpose
Defines the criteria for selecting code to train our educational model.

## Allowed Code
*   **High Quality:** Well-commented, standard Python code.
*   **Educational:** Algorithms, data structures, clean utility functions.
*   **Self-Contained:** Functions or classes that make sense in isolation.

## Forbidden Code
*   **Malicious:** Code intended to harm systems or steal data.
*   **Obfuscated:** Minified or intentionally unreadable code.
*   **PII:** Code containing API keys, passwords, or personal names.
*   **Complex Frameworks:** Deeply nested enterprise boilerplate that distracts from language syntax.

## Why Small, Clean Data?
1.  **Observability:** With a small dataset (2k-5k functions), we can manually inspect inputs and trace model behavior.
2.  **Training Speed:** Allows for rapid iteration on consumer hardware.
3.  **Educational Clarity:** Learning from "textbook" code reduces noise and helps the model grasp syntax fundamentals faster.
