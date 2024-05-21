#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the Star Wars API URL for films
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the Star Wars API
request(apiUrl, function (err, response, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  // Parse the JSON response
  const filmData = JSON.parse(body);

  // Define a function to fetch character data and print names
  function fetchAndPrintCharacter (index) {
    if (index >= filmData.characters.length) {
      return; // End of characters list
    }

    // Make a GET request to the character URL
    request(filmData.characters[index], function (err, response, body) {
      if (err) {
        console.error('Error:', err);
        return;
      }

      // Parse the JSON response for character data
      const characterData = JSON.parse(body);

      // Print the character name
      console.log(characterData.name);

      // Continue fetching and printing next character
      fetchAndPrintCharacter(index + 1);
    });
  }

  // Start fetching and printing characters from index 0
  fetchAndPrintCharacter(0);
});
