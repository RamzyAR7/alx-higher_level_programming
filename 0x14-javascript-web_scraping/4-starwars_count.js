#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present.

const argv = process.argv;
const request = require('request');

if (argv.length < 3) {
  console.log('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const apiUrl = argv[2];
const characterId = 18;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const data = JSON.parse(body);
  let movieCount = 0;
  data.results.forEach(film => {
    // Check if character ID 18 (Wedge Antilles) is in the characters array
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      movieCount++;
    }
  });

  // Print the count of movies
  console.log(movieCount);
});
