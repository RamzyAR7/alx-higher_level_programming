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

  rotate () {
    const swp = this.height;
    this.height = this.width;
    this.width = swp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
