import sentencepiece as spm
from pathlib import Path

def inspect(text, model_path):
    """
    Loads tokenizer and prints the list of tokens for the given text.
    """
    if not Path(model_path).exists():
        print(f"Error: Model file {model_path} not found.")
        return

    sp = spm.SentencePieceProcessor(model_file=model_path)
    
    # Encode as pieces (strings) and IDs
    tokens = sp.encode_as_pieces(text)
    ids = sp.encode_as_ids(text)
    
    print("-" * 40)
    print(f"Input Text:\n{text}")
    print("-" * 40)
    print(f"{'ID':<6} | {'Token':<20}")
    print("-" * 40)
    
    for i, t in zip(ids, tokens):
        # Escape special chars for visibility
        visible_t = t.replace(' ', ' ')  # SentencePiece uses   (U+2581) for space
        print(f"{i:<6} | {visible_t:<20}")
    print("-" * 40)

if __name__ == "__main__":
    model_file = "tokenizer/code_tokenizer.model"
    
    sample_code = """def hello():
    print('world')"""
    
    # Try a few samples including the ones we care about (indentation)
    inspect(sample_code, model_file)
    
    print("\n\n")
    sample_math = "result = a + b * c"
    inspect(sample_math, model_file)
