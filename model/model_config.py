from transformers import GPT2Config

# We use a very small model for educational purposes
# params ~ N_LAYER * N_EMBD^2 * 12
# 6 * 256^2 * 12 = 4.7M params (Tiny!)
# This ensures it trains in minutes on CPU/low-end GPU.

VOCAB_SIZE = 500 # Matches our tokenizer
CONTEXT_LENGTH = 128 # Small context window

def get_config():
    return GPT2Config(
        vocab_size=VOCAB_SIZE,
        n_positions=CONTEXT_LENGTH,
        n_ctx=CONTEXT_LENGTH,
        n_embd=256,
        n_layer=6,
        n_head=8,
        activation_function="gelu_new",
        resid_pdrop=0.1,
        embd_pdrop=0.1,
        attn_pdrop=0.1,
        bos_token_id=2, # Matches SentencePiece [BOS]
        eos_token_id=3, # Matches SentencePiece [EOS]
    )
