#!/usr/bin/node
function Factorial (x) {
	if (x === 0) {
		return (1);
	}
	return (Factorial(x - 1) * x);
}
const arg = process.argv[2];
let res;

if (!arg || isNaN(arg) || arg === 1) {
	res = 1;
}
else {
	res = Factorial(parseInt(arg));
}
console.log(res);
