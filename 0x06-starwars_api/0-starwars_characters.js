#!/usr/bin/node

const request = require('request');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Make a request to the Star Wars API to fetch the movie details
request(`https://swapi.dev/api/films/${movieId}/`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    // Fetch each character's details
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
