#!/usr/bin/node
/*  class Rectangle that defines a rectangle
    with conditional the sides if it's 0 or negative */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
