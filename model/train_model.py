import torch
from torch.utils.data import Dataset
from transformers import GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
import sentencepiece as spm
from pathlib import Path
import model_config

# Paths
TOKENIZER_MODEL = "tokenizer/code_tokenizer.model"
TRAIN_FILE = "data/processed/train.txt"
VAL_FILE = "data/processed/val.txt"
OUTPUT_DIR = "model_output"

class CodeDataset(Dataset):
    def __init__(self, file_path, sp_model_path, block_size=128):
        self.block_size = block_size
        
        # Load Tokenizer
        self.sp = spm.SentencePieceProcessor(model_file=sp_model_path)
        
        # Load Data
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            
        # Encode everything at once (for simplicity in this small scale)
        # In production, we would stream or memory-map.
        self.tokens = self.sp.encode_as_ids(text)
        print(f"Loaded {len(self.tokens)} tokens from {file_path}")

    def __len__(self):
        # We return chunks of block_size
        return len(self.tokens) // self.block_size

    def __getitem__(self, idx):
        # Calculate start/end
        start = idx * self.block_size
        end = start + self.block_size
        
        chunk = self.tokens[start:end]
        
        # Inputs = Labels for Causal LM (shifted inside the model)
        # We must return tensor
        return {
            "input_ids": torch.tensor(chunk, dtype=torch.long),
            "labels": torch.tensor(chunk, dtype=torch.long)
        }

def train():
    # 1. Setup Data
    print("Loading datasets...")
    train_dataset = CodeDataset(TRAIN_FILE, TOKENIZER_MODEL, block_size=model_config.CONTEXT_LENGTH)
    val_dataset = CodeDataset(VAL_FILE, TOKENIZER_MODEL, block_size=model_config.CONTEXT_LENGTH)
    
    # 2. Setup Model
    print("Initializing model...")
    config = model_config.get_config()
    model = GPT2LMHeadModel(config)
    print(f"Model parameters: {model.num_parameters() / 1e6:.2f}M")
    
    # 3. Setup Trainer
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=5,           # Small dataset, can epoch more
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_steps=10,
        learning_rate=5e-4,
        weight_decay=0.01,
        report_to="none",             # Disable wandb/tensorboard for simplicity
        use_cpu=False if torch.cuda.is_available() else True
    )
    
    # We don't need a special collator because our dataset already returns fixed size tensors
    # default_data_collator handles stacking tensors.
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
    )
    
    # 4. Train
    print("Starting training...")
    trainer.train()
    
    # 5. Save
    print("Saving model...")
    model.save_pretrained(OUTPUT_DIR)
    print("Done.")

if __name__ == "__main__":
    train()
