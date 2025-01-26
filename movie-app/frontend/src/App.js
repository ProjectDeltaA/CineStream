import React, { useState, useEffect } from "react";
import axios from "axios";

const App = () => {
  const [movies, setMovies] = useState([]);
  const [newMovie, setNewMovie] = useState({ title: "", genre: "" });

  const fetchMovies = async () => {
    const response = await axios.get("http://localhost:5000/movies");
    setMovies(response.data);
  };

  useEffect(() => {
    fetchMovies();
  }, []);

  const addMovie = async () => {
    await axios.post("http://localhost:5000/movies", newMovie);
    fetchMovies();
  };

  return (
    <div>
      <h1>Movie App</h1>
      <input
        type="text"
        placeholder="Title"
        onChange={(e) => setNewMovie({ ...newMovie, title: e.target.value })}
      />
      <input
        type="text"
        placeholder="Genre"
        onChange={(e) => setNewMovie({ ...newMovie, genre: e.target.value })}
      />
      <button onClick={addMovie}>Add Movie</button>
      <ul>
        {movies.map((movie) => (
          <li key={movie.title}>{movie.title} - {movie.genre}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;