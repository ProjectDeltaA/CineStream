from flask import Flask, request, jsonify
from pymongo import MongoClient
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('request_count', 'Number of requests received', ['method', 'endpoint'])

# MongoDB Setup
client = MongoClient('mongodb://db:27017/')
db = client['moviesdb']
movies_collection = db['movies']

@app.before_request
def before_request():
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/movies', methods=['GET'])
def get_movie():
    name = request.args.get('name')
    movie = movies_collection.find_one({"name": name})
    if movie:
        movie.pop('_id')  # Remove the MongoDB ObjectID
        return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

@app.route('/movies', methods=['POST'])
def update_movie():
    data = request.json
    result = movies_collection.update_one(
        {"name": data['name']},
        {"$set": {
            "genre": data['genre'],
            "year": data['year'],
            "rank": data.get('rank', None),
            "description": data.get('description', "")
        }},
        upsert=True
    )
    return jsonify({"message": "Movie updated successfully"}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)