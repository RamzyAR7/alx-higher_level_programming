#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      let x, y;
      for (x = 0; x < this.height; x++) {
        let rec = '';
        for (y = 0; y < this.width; y++) {
          rec += c;
        }
        console.log(rec);
      }
    }
  }
}

module.exports = Square;
