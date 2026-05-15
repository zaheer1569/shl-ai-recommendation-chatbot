import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

products = data["products"]
embeddings = data["embeddings"]

def recommend(query, top_k=3):
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, embeddings)[0]

    ranked = sorted(
         zip(products, similarities),
         key=lambda x: x[1],
         reverse=True
    )

    return [item[0] for item in ranked[:top_k]]