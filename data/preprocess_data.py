"""
Script: Preprocess Data
Purpose: Combine raw text files, clean them, and split into train/val sets.
"""

import os
import random
from pathlib import Path

# Configuration
RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")
TRAIN_RATIO = 0.9
SEED = 42

def clean_content(text):
    """
    Basic cleaning: remove excessive newlines, normalize line endings.
    Since we are doing code, we must preserve indentation!
    """
    # Normalize line endings
    text = text.replace('\r\n', '\n')
    
    # Optional: Remove multiple trailing empty lines at end of file
    text = text.strip() + "\n"
    
    return text

def preprocess():
    print(f"Scanning {RAW_DATA_DIR}...")
    
    all_files = list(RAW_DATA_DIR.glob("*.txt"))
    if not all_files:
        print("No .txt files found in data/raw!")
        return

    all_content = []
    
    for file_path in all_files:
        print(f"Reading {file_path.name}...")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # We treat each FILE as a separate continuous block for now,
                # or we could split by function if we parsed it.
                # For simplicity, we'll just append them with a separator.
                cleaned = clean_content(content)
                all_content.append(cleaned)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Combine all content
    # We use a special separator if we want, or just newlines.
    # LLMs often train on concatenated files.
    full_text = "\n\n".join(all_content)
    
    # Split into Train/Val
    # Splitting by CHARACTER or LINE is risky for code (breaking functions).
    # Ideally we split by logical blocks (functions). 
    # Whatever, let's splits by 'def ' occurrences for better granularity?
    # Or just keep it simple: split the list of FILES (coarse grain) or chunks.
    
    # Let's split by files to preserve function integrity within files
    random.seed(SEED)
    random.shuffle(all_content)
    
    split_idx = int(len(all_content) * TRAIN_RATIO)
    train_docs = all_content[:split_idx]
    val_docs = all_content[split_idx:]
    
    # If we have very few files (e.g. 4), this split might result in empty val.
    # Check and enforce at least one val doc if possible.
    if not val_docs and len(all_content) > 1:
        val_docs = [train_docs.pop()]
        
    print(f"Split: {len(train_docs)} training docs, {len(val_docs)} validation docs.")

    # Write outputs
    train_path = PROCESSED_DATA_DIR / "train.txt"
    val_path = PROCESSED_DATA_DIR / "val.txt"
    
    with open(train_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(train_docs))
        
    with open(val_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(val_docs))
        
    print(f"Saved processed data to {PROCESSED_DATA_DIR}")

if __name__ == "__main__":
    # Ensure directories exist
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    preprocess()
