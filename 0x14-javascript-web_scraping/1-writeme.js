#!/usr/bin/node
// a script that writes a string to a file.

const argv = process.argv;
const file = argv[2];
const txt = argv[3];

const fs = require('fs');
fs.writeFile(file, txt, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
