import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from flask import Flask, request, jsonify, render_template
import os
nltk.download('punkt')
nltk.download('stopwords')

faqs = {
    "hi" : "Hello There! How can i Help You?",
    "Where Is my order": "your order was just arrived to xyz town , will reach you by tomorrow Evening.",
    "What are your hours of working": "Our hours of operation are 9 AM to 5 PM, Monday to Friday.",
    "Where are you located?": "We are located at 123 Main Street, X Town, India.",
    "How can I contact support": "You can contact support via email at support@example.com or call us at +91 6333942222",
    "Did your company support international shipping": " Yes we support International shipping of the product"
}

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    return ' '.join(filtered_tokens)

preprocessed_faqs = {preprocess(q): a for q, a in faqs.items()}

def preprocess_query(query):
    return preprocess(query)

def find_best_match(query, faqs):
    preprocessed_query = preprocess_query(query)
    for q in faqs:
        if preprocessed_query in q:
            return faqs[q]
    return "I'm sorry, I don't understand the question."

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = find_best_match(user_input, preprocessed_faqs)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

