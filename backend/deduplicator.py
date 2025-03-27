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

if __name__ == "__main__":
    example_email = {
        "subject": "Request for Adjustment - Reallocation Fees",
        "body": "Dear Support Team, \n\nWe need to request an adjustment for reallocation fees for Deal XYZ. The amount is $25,000."
    }
    example_email2 = {
        "subject": "Request for Adjustment - Reallocation Fees",
        "body": "Dear Support Team, \n\nWe need to request an adjustment for reallocation fees for Deal XYZ. The amount is $25,000."
    }
    result = check_duplicate(example_email)
    print(result)
    result2 = check_duplicate(example_email2)
    print(result2)
