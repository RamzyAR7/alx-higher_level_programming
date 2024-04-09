#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
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
