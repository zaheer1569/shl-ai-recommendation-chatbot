from sentence_transformers import SentenceTransformer
import json
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("catalog.json", "r", encoding="utf-8") as f:
    products = json.load(f)

texts = [p["description"] for p in products]

embeddings = model.encode(texts)

with open("embeddings.pkl", "wb") as f:
    pickle.dump({
        "products": products,
        "embeddings": embeddings
    }, f)

print("Embeddings saved!")