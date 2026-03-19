from sentiment_model import vectorizer, model

text = ["This product is amazing"]

vector = vectorizer.transform(text)

prediction = model.predict(vector)

print(prediction)