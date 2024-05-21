#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const argv = process.argv;
const request = require('request');

if (argv.length < 3) {
  console.log('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (err, response, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const data = JSON.parse(body);

  if (response.statusCode === 200) {
    console.log(data.title);
  } else {
    console.log('Error:', data.detail || 'Unknown error');
  }
});
