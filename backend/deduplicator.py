from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)  # 384-dim vector

def check_duplicate(email):
    vector = model.encode(email["body"]).reshape(1, -1)
    if index.ntotal > 0:
        D, I = index.search(vector, 1)
        if D[0][0] < 0.1:  # Similarity threshold
            return True
    index.add(vector)
    return False
