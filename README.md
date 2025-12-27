# Coding LLM Education: Causal Language Modeling Research

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/Status-Experimental-orange.svg)]()

## Overview
**Coding LLM Education** is an open-source research initiative designed to demystify the internal mechanics of Large Language Models (LLMs) specialized in code generation. By building a causal transformer from scratch (~5M parameters), this project provides a "glass box" environment for studying tokenization quirks, hallucination patterns, and the trust boundaries of AI-generated software.

## Key Features
*   **Custom BPE Tokenizer:** Specialized SentencePiece model optimized for Python syntax.
*   **Transparent Architecture:** Minimalistic GPT-2 implementation for educational inspection.
*   **Failure Analysis:** Dedicated datasets and experiments to document model hallucinations and logic failures.
*   **Instruction Tuning:** Pipeline for fine-tuning base models on instruction-response pairs.

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/coding-llm-education.git

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r environment/requirements.txt
```

## Usage

### 1. Preprocess Data
Prepare the raw code snippets for training:
```bash
python data/preprocess_data.py
```

### 2. Train Tokenizer & Model
Train the SentencePiece tokenizer and the base transformer model:
```bash
python tokenizer/train_tokenizer.py
python model/train_model.py
```

### 3. Evaluate
Test the model's generation capabilities:
```bash
python model/evaluate_model.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This software is for **educational and research purposes only**. It is not intended for production use. Generated code should be reviewed carefully before execution.
