#!/usr/bin/node

let arg1, arg2;
if (process.argv[2]) {
  arg1 = process.argv[2];
}
if (process.argv[3]) {
  arg2 = process.argv[3];
}
console.log(arg1 + ' is ' + arg2);
