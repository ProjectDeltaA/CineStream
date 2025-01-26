db = db.getSiblingDB("movieApp");
db.createCollection("movies");
db.movies.insertMany([
    { title: "Inception", genre: "Sci-Fi", year: 2010 },
    { title: "The Dark Knight", genre: "Action", year: 2008 }
]);