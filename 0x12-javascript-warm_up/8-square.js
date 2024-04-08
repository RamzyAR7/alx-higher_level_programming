#!/usr/bin/node
const arg = process.argv[2];

let count = '';
let i, x;
for (i = 1; i <= arg; i++) {
	for (x = 0; x < arg; x++) {
		count += 'x';
	}
	if (i != arg) {
		count += '\n';
	}
}
console.log(count);
