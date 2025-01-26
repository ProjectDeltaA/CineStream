from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://movieapp-mongo:27017/")
db = client["movieApp"]
movies_collection = db["movies"]

@app.route("/movies", methods=["GET"])
def get_movies():
    movies = list(movies_collection.find({}, {"_id": 0}))
    return jsonify(movies)

@app.route("/movies", methods=["POST"])
def create_movie():
    data = request.json
    movies_collection.insert_one(data)
    return jsonify({"message": "Movie added successfully!"}), 201

@app.route("/movies/<title>", methods=["PUT"])
def update_movie(title):
    data = request.json
    movies_collection.update_one({"title": title}, {"$set": data})
    return jsonify({"message": "Movie updated successfully!"})

@app.route("/movies/<title>", methods=["DELETE"])
def delete_movie(title):
    movies_collection.delete_one({"title": title})
    return jsonify({"message": "Movie deleted successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)