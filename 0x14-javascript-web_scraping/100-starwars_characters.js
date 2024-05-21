#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the Star Wars API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the Star Wars API
request(apiUrl, function (err, response, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Print the character names
  data.characters.forEach(characterUrl => {
    request(characterUrl, function (err, response, body) {
      if (err) {
        console.error('Error:', err);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
