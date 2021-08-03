#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      let ch;
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          ch = 'X';
        } else {
          ch = c;
        }
        row += ch;
      }
      console.log(row + '');
    }
  }
}

module.exports = Square;
