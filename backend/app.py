from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

app = Flask(__name__)

# Cargar el modelo y el tokenizador
model_path = './sentiment_pipeline'
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.softmax(outputs.logits, dim=-1)

    predicted_label = torch.argmax(predictions, dim=1).item()
    predicted_confidence = predictions[0][predicted_label].item()

    return jsonify({
        'label': predicted_label,
        'confidence': predicted_confidence
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
