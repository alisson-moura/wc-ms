from flask import Flask, request, jsonify
from flask_expects_json import expects_json
from src.wordcloud.index import generate_wordcloud_json

app = Flask(__name__)

schema = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "feedback": {"type": "string"},
                    "score": {"type": "string"}
                },
                "required": ["feedback", "score"]
            }
        }
    }
}


@app.route('/wc/generate', methods=['POST'])
@expects_json(schema)
def generate():
    try:
        data = request.get_json()
        result = generate_wordcloud_json(data)
        return result, 201
    except Exception as e:
        print(e)
        return {"error": "An error occurred" }, 500
