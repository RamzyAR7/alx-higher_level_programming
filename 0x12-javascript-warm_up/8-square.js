#!/usr/bin/node
const arg = process.argv[2];

let i, x;
for (i = 1; i <= arg; i++) {
  let count = '';
  for (x = 0; x < arg; x++) {
    count += 'x';
  }
  console.log(count);
}
