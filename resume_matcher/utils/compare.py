from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
import numpy as np


def calculate_match_score(resume_text: str, jd_text: str) -> float:
    """Returns a match score (0-100) using TF-IDF + cosine similarity."""
    texts = [resume_text or "", jd_text or ""]
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    try:
        tfidf = vectorizer.fit_transform(texts)
        sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return round(float(sim) * 100, 2)
    except Exception:
        return 0.0


def extract_top_keywords(text: str, top_n=10):
    """Simple keyword extraction using TF-IDF vocabulary weights."""
    if not text or text.strip() == "":
        return []
    vectorizer = TfidfVectorizer(stop_words="english", max_features=2000)
    tfidf = vectorizer.fit_transform([text])
    feature_array = np.array(vectorizer.get_feature_names_out())
    tfidf_sorting = np.argsort(tfidf.toarray()).flatten()[::-1]
    top_n = min(top_n, feature_array.shape[0])
    top_keywords = feature_array[tfidf_sorting][:top_n].tolist()
    return top_keywords