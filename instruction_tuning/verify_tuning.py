"""
Script: Verify Tuning
Purpose: Test if the model learned to follow instructions after fine-tuning.
"""
import torch
from transformers import GPT2LMHeadModel
import sentencepiece as spm
import sys
import os

# Ensure we can import from model/ directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
import model_config

MODEL_PATH = "model_tuned"
TOKENIZER_MODEL = "tokenizer/code_tokenizer.model"

def generate(model, sp, instruction, max_len=100):
    # Format prompt exactly as in training
    prompt = f"Instruction: {instruction}\nOutput:"
    
    input_ids = sp.encode_as_ids(prompt)
    input_tensor = torch.tensor([input_ids], dtype=torch.long)
    
    with torch.no_grad():
        output_ids = model.generate(
            input_tensor, 
            max_length=max_len, 
            num_return_sequences=1,
            do_sample=True,
            temperature=0.3, # Low temp for precision/memorization
            pad_token_id=0,
            eos_token_id=3
        )
    
    full_text = sp.decode(output_ids[0].tolist())
    # Extract just the output part
    if "Output:" in full_text:
        return full_text.split("Output:", 1)[1].strip()
    return full_text

if __name__ == "__main__":
    if not os.path.exists(MODEL_PATH):
        print(f"Error: {MODEL_PATH} not found. Wait for training to finish.")
        sys.exit(1)
        
    print("Loading tuned model...")
    model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)
    model.eval()
    sp = spm.SentencePieceProcessor(model_file=TOKENIZER_MODEL)
    
    test_instructions = [
        "Create a function that adds two numbers.",
        "How do I import matplotlib?",
        "Write a conditional to check if x is positive.",
        "Write a function that returns the sum of a list."
    ]
    
    print("\n" + "="*40)
    print("INSTRUCTION TUNING VERIFICATION")
    print("="*40)
    
    for inst in test_instructions:
        print(f"\nInstruction: {inst}")
        print("-" * 20)
        result = generate(model, sp, inst)
        print(result)
        print("-" * 20)
