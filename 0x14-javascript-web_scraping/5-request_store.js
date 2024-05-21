#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, function (err, response, body) {
  if (err) {
    console.error('Error:', err);
  }

  // Write the response body to the specified file in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.error('Error:', err);
    }
  });
});
