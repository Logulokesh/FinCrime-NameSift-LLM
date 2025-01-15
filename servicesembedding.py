import numpy as np
from sentence_transformers import SentenceTransformer
from config import config

class EmbeddingGenerator:
    def __init__(self):
        self.embedding_size = config.EMBEDDING_SIZE  # 1536 from config.py
        # Use local model path
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Outputs 384 dims

    def generate_embedding(self, text: str):
        embedding = self.model.encode(text, convert_to_numpy=True)  # 384 elements
        # Pad to 1536 if shorter
        if len(embedding) < self.embedding_size:
            embedding = np.pad(embedding, (0, self.embedding_size - len(embedding)), mode='constant', constant_values=0)
        return embedding[:self.embedding_size].tolist()  # Ensure exact length 1536