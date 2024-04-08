#!/usr/bin/node
const arg = process.argv[2];

if (!arg) {
  console.log('Missing size');
} else {
  let i, x;
  for (i = 0; i < arg; i++) {
    let count = '';
    for (x = 0; x < arg; x++) {
      count += 'X';
    }
    console.log(count);
  }
}
