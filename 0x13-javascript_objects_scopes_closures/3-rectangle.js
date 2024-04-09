#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x, y;
    for (x = 0; x < this.height; x++) {
      let rec = '';
      for (y = 0; y < this.width; y++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
}

module.exports = Rectangle;
