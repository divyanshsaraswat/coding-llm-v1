import sentencepiece as spm
from pathlib import Path

def train_tokenizer(input_file, vocab_size=2000, model_prefix='code_tokenizer'):
    """
    Trains a SentencePiece tokenizer.
    
    Args:
        input_file (str): Path to text file containing code samples.
        vocab_size (int): Target vocabulary size. Small vocab for educational inspection.
        model_prefix (str): Output filename prefix (without extension).
    """
    print(f"Training tokenizer on {input_file} with vocab size {vocab_size}...")
    
    # SentencePiece treats the input as a single stream.
    # We use byte-pair-encoding (BPE) which is standard for LLMs.
    # character_coverage=1.0 ensures all characters are included (important for code symbols).
    spm.SentencePieceTrainer.train(
        input=input_file,
        model_prefix=model_prefix,
        vocab_size=vocab_size,
        model_type='bpe',
        character_coverage=1.0,
        pad_id=0,
        unk_id=1,
        bos_id=2,
        eos_id=3,
        pad_piece='[PAD]',
        unk_piece='[UNK]',
        bos_piece='[BOS]',
        eos_piece='[EOS]',
        user_defined_symbols=['  ', '    '], # Explicitly handle indentation
    )
    
    print(f"Training complete. Saved {model_prefix}.model and {model_prefix}.vocab")

if __name__ == "__main__":
    # Define paths relative to this script or project root
    # Assuming script is run from project root: python tokenizer/train_tokenizer.py
    
    input_path = Path("data/processed/train.txt")
    output_prefix = "tokenizer/code_tokenizer"
    
    if not input_path.exists():
        print(f"Error: {input_path} not found. Run preprocessing first.")
    else:
        train_tokenizer(str(input_path), vocab_size=500, model_prefix=output_prefix)
