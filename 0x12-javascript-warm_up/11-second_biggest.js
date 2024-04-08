#!/usr/bin/node

const arg = process.argv.slice(2).map(Number);

if (arg.length < 2) {
  console.log(0);
} else {
  let max = arg[0];
  let max2 = arg[1];

  for (let i = 1; i < arg.length; i++) {
    if (arg[i] > max) {
      max2 = max;
      max = arg[i];
    }
    if (arg[i] > max2 && arg[i] < max) {
      max2 = arg[i];
    }
  }

  console.log(max2);
}
