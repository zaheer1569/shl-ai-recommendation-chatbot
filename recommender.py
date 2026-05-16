import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("catalog.json", "r", encoding="utf-8") as f:
    products = json.load(f)

texts = [
    f"{item.get('name', '')} {item.get('description', '')}"
    for item in products
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

def recommend(query, top_k=3):
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    ranked_indices = similarities.argsort()[::-1][:top_k]

    return [products[i] for i in ranked_indices]