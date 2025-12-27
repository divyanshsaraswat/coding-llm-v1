"""
Script: Run Experiments
Purpose: systematically run the prompts defined in experiments/prompt_tests.md and log results.
"""
import torch
from transformers import GPT2LMHeadModel
import sentencepiece as spm
import pandas as pd
from pathlib import Path

MODEL_PATH = "model_output"
TOKENIZER_MODEL = "tokenizer/code_tokenizer.model"
OUTPUT_FILE = "experiments/experiment_results.csv"

def load_resources():
    print("Loading model and tokenizer...")
    model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)
    model.eval()
    sp = spm.SentencePieceProcessor(model_file=TOKENIZER_MODEL)
    return model, sp

def generate(model, sp, prompt, max_len=50):
    input_ids = sp.encode_as_ids(prompt)
    input_tensor = torch.tensor([input_ids], dtype=torch.long)
    
    with torch.no_grad():
        output_ids = model.generate(
            input_tensor, 
            max_length=max_len, 
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            pad_token_id=0,
            eos_token_id=3
        )
    return sp.decode(output_ids[0].tolist())

def run_experiments():
    model, sp = load_resources()
    
    # Define the experiments from prompt_tests.md
    # We automate this list
    experiments = [
        {"type": "Zero-Shot", "prompt": "def factorial(n):", "expected": "Recursive function"},
        {"type": "Zero-Shot", "prompt": "import matplotlib.pyplot as", "expected": "plt"},
        {"type": "Zero-Shot", "prompt": "class User:", "expected": "__init__ method"},
        {"type": "Zero-Shot", "prompt": "def is_palindrome(s):", "expected": "Check string reversal"},
        {"type": "Failure-Check", "prompt": "while True:", "expected": "Infinite loop or break"},
        {"type": "Failure-Check", "prompt": "from sklearn.metrics import", "expected": "Valid metric or Hallucination"},
    ]
    
    results = []
    
    print(f"Running {len(experiments)} experiments...")
    
    for exp in experiments:
        prompt = exp["prompt"]
        print(f"Testing: {prompt}")
        
        # Generate 3 samples to see variety
        output = generate(model, sp, prompt)
        
        results.append({
            "type": exp["type"],
            "prompt": prompt,
            "expected": exp["expected"],
            "actual_output": output.replace("\n", "\\n")[:100] + "..." # Truncate for CSV
        })
        
    # Save results
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Results saved to {OUTPUT_FILE}")
    
    # Also append to the Markdown file for easy reading
    with open("experiments/prompt_tests.md", "a", encoding="utf-8") as f:
        f.write("\n\n## Automated Run Results\n")
        f.write(df.to_markdown(index=False))

if __name__ == "__main__":
    run_experiments()
