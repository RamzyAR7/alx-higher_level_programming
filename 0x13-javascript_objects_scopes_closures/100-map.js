#!/usr/bin/node
const lists = require('./100-data.js').list;

const newList = lists.map((value, index) => value * index);

console.log(lists);
console.log(newList);
