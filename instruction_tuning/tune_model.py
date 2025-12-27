import torch
from torch.utils.data import Dataset
from transformers import GPT2LMHeadModel, Trainer, TrainingArguments
import sentencepiece as spm
import json
import sys
import os

# Ensure we can import from model/ directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
import model_config

# Paths
MODEL_PATH = "model_output" # Start from pre-trained model
TOKENIZER_MODEL = "tokenizer/code_tokenizer.model"
INSTRUCTION_FILE = "instruction_tuning/instructions.jsonl"
OUTPUT_DIR = "model_tuned"

class InstructionDataset(Dataset):
    def __init__(self, file_path, sp_model_path, block_size=128):
        self.block_size = block_size
        self.sp = spm.SentencePieceProcessor(model_file=sp_model_path)
        self.samples = []
        
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                # Format: "Instruction: ... \nOutput: ..."
                # This helps the model know when to start generating code.
                text = f"Instruction: {data['instruction']}\nOutput: {data['output']}"
                self.samples.append(text)
        
        print(f"Loaded {len(self.samples)} instruction samples.")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        text = self.samples[idx]
        ids = self.sp.encode_as_ids(text)
        
        # Pad or Truncate to fixed length
        if len(ids) > self.block_size:
            ids = ids[:self.block_size]
        else:
            padding = [0] * (self.block_size - len(ids))
            ids = ids + padding
            
        tensor = torch.tensor(ids, dtype=torch.long)
        
        # Mask padding in labels (0 -> -100) so we don't calculate loss on padding
        labels = torch.tensor([i if i != 0 else -100 for i in ids], dtype=torch.long)
        
        return {
            "input_ids": tensor,
            "labels": labels
        }

def fine_tune():
    print("Loading base model...")
    # Load the PRE-TRAINED model we just made
    model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)
    
    print("Preparing dataset...")
    # We use the same dataset for train and val because it's tiny (overfitting target)
    train_dataset = InstructionDataset(INSTRUCTION_FILE, TOKENIZER_MODEL, block_size=model_config.CONTEXT_LENGTH)
    
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=50,          # High epochs to force memorization of instructions
        per_device_train_batch_size=4,
        learning_rate=1e-4,           # Lower LR than pre-training
        logging_steps=5,
        save_steps=1000,              # Don't save every step
        save_strategy="no",           # Save only at end
        report_to="none",
        use_cpu=False if torch.cuda.is_available() else True
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )
    
    print("Starting fine-tuning...")
    trainer.train()
    
    print("Saving tuned model...")
    model.save_pretrained(OUTPUT_DIR)
    print("Done.")

if __name__ == "__main__":
    fine_tune()
