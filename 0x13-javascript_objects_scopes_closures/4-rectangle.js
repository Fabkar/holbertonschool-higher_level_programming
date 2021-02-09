#!/usr/bin/node
/* class Rectangle that defines a rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { // Conditional when the sides are greater than 0
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) { // for each space print an X with the size of rectangle
      console.log('X'.repeat(this.width));
    }
  }

  rotate () { // that exchanges the width and the height of the rectangle
    const i = this.width;
    this.width = this.height;
    this.height = i;
  }

  double () { // that multiples the width and the height of the rectangle by 2.
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
