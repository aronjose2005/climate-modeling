from transformers import pipeline

# Analyze environmental data using NLP
def analyze_environmental_data(data_text):
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_analyzer(data_text)[0]
    sentiment = "positive" if result["label"] == "POSITIVE" else "negative"
    return {"sentiment": sentiment, "score": result["score"], "text": data_text}
