import pandas as pd
from pymongo import MongoClient

def seed_db():
    client = MongoClient('mongodb://db:27017/')
    db = client['moviesdb']
    movies_collection = db['movies']
    df = pd.read_csv('IMDB-Movie-Data.csv')
    for _, row in df.iterrows():
        movies_collection.update_one(
            {"name": row['Title']},
            {"$set": {
                "genre": row['Genre'],
                "year": int(row['Year']),
                "rank": int(row['Rank']),
                "description": row['Description']
            }},
            upsert=True
        )

if __name__ == "__main__":
    seed_db()