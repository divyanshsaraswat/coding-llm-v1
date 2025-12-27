# Instruction Tuning Data
# Purpose: Define the format for instruction-response pairs to "teach" the model to follow commands.

## Format
We will use a simple JSONL format:
```json
{"instruction": "Write a function to sum a list.", "input": "", "output": "def sum_list(L):\n    return sum(L)"}
```

## Data Sources
*   Hand-written examples (high quality).
*   Filtered subsets from open datasets (e.g., Alpaca) - ONLY code-related.
