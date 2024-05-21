#!/usr/bin/node
// a script that display the status code of a GET request.

const argv = process.argv;
const request = require('request');

if (argv.length < 3) {
  console.log('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, function (err, response) {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('code:', response.statusCode);
  }
});
