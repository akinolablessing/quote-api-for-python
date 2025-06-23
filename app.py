from flask import Flask, request, jsonify
from model.quoteModel import Quote
from storage.quoteStorage import quote_storage

app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to the Quote API."
@app.route("/quotes/get", methods=["GET"])
def get_quotes():
    return jsonify([quote.__dict__ for quote in quote_storage.get_all()]), 200

@app.route("/quotes/post", methods=["POST"])
def add_quote():
    data = request.get_json()
    author = data.get("author")
    content = data.get("content")

    if not author or not content:
        return jsonify({"error": "Author and content are required."}), 400

    quote = Quote(author=author, content=content)
    quote_storage.add(quote)
    return jsonify({"message": "Quote added successfully."}), 201

if __name__ == "__main__":
    app.run(debug=True)