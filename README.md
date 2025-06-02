
# FAQ Chatbot with NLTK

This project is a simple FAQ chatbot built using Python and the `nltk` (Natural Language Toolkit) library. The chatbot processes user queries, matches them to a predefined set of FAQs, and returns the appropriate response.

## Features

- Predefined FAQ responses for common queries such as working hours, order status, and contact information.
- Text preprocessing using `nltk` for tokenization, case normalization, and stopword removal.
- Simple text-matching algorithm for determining the best response based on user input.

## Prerequisites

Ensure you have Python installed, along with the following libraries:

```bash
pip install nltk
```

Additionally, you need to download some `nltk` resources for tokenization and stopword removal:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## How It Works

- The chatbot processes the user's input using natural language processing (NLP) techniques.
- It uses `nltk` to tokenize the input, convert it to lowercase, remove non-alphanumeric tokens, and filter out stopwords.
- The preprocessed user query is compared against preprocessed FAQ questions to find the best match.
- If a match is found, the corresponding FAQ answer is returned; otherwise, a default message is sent.

### Example FAQs

The chatbot can respond to common queries such as:

- "Where is my order?"
- "What are your hours of operation?"
- "Where are you located?"
- "How can I contact support?"
- "Do you support international shipping?"

## Code Structure

```bash
├── chatbot.py          # The main Python script for the chatbot
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Rajesh4619/Chatbot.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Python script:

```bash
python app.py
```

4. The chatbot will prompt for input in the terminal. You can ask questions, and it will respond based on the predefined FAQs.

## Example

```bash
> User: Where is my order?
> Bot: Your order was just arrived to xyz town, will reach you by tomorrow evening.

> User: What are your hours of working?
> Bot: Our hours of operation are 9 AM to 5 PM, Monday to Friday.
```

## Future Enhancements

- Improve the matching algorithm to use more advanced techniques like similarity measures or machine learning.
- Expand the FAQ list to include more responses and variations in phrasing.
- Integrate the chatbot with a web interface or messaging platform for easier user interaction.

