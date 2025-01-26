const fs = require('fs');
const csv = require('csv-parser');

db = db.getSiblingDB("movieApp");

// Create the collection
db.createCollection("movies");

// Read CSV file and insert data
const movies = [];
const csvFilePath = 'IMDB-Movie-Data.csv';

fs.createReadStream(csvFilePath)
  .pipe(csv())
  .on('data', (row) => {
    movies.push({
      title: row.Title,
      genre: row.Genre,
      year: parseInt(row.Year)
    });
  })
  .on('end', () => {
    db.movies.insertMany(movies);
    print('Movies imported successfully!');
  });
