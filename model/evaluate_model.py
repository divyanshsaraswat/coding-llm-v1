import torch
from transformers import GPT2LMHeadModel
import sentencepiece as spm
import model_config

MODEL_PATH = "model_output"
TOKENIZER_MODEL = "tokenizer/code_tokenizer.model"

def load_model():
    print(f"Loading model from {MODEL_PATH}...")
    model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)
    model.eval()
    return model

def load_tokenizer():
    sp = spm.SentencePieceProcessor(model_file=TOKENIZER_MODEL)
    return sp

def generate_samples(prompt, model, sp, max_length=50, temperature=0.7):
    """
    Generates code completion for a given prompt.
    """
    input_ids = sp.encode_as_ids(prompt)
    input_tensor = torch.tensor([input_ids], dtype=torch.long)
    
    # Generate
    with torch.no_grad():
        output_ids = model.generate(
            input_tensor, 
            max_length=max_length, 
            num_return_sequences=1,
            do_sample=True,
            temperature=temperature,
            pad_token_id=0, # SPM [PAD]
            eos_token_id=3  # SPM [EOS]
        )
    
    # Decode
    generated_text = sp.decode(output_ids[0].tolist())
    return generated_text

if __name__ == "__main__":
    model = load_model()
    sp = load_tokenizer()
    
    test_prompts = [
        "def fibonacci(n):",
        "def add(a, b):",
        "class User:",
        "import "
    ]
    
    print("\n" + "="*40)
    print("MODEL GENERATION TESTS")
    print("="*40)
    
    for p in test_prompts:
        print(f"\nPrompt: {p}")
        result = generate_samples(p, model, sp)
        print("-" * 20)
        print(result)
        print("-" * 20)
