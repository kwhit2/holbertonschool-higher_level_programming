#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const i = this.width;
    const k = this.height;
    this.width = k;
    this.height = i;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
