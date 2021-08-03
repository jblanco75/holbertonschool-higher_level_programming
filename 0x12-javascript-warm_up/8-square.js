#!/usr/bin/node

const dim = parseInt(process.argv[2]);
if (isNaN(dim)) {
  console.log('Missing size');
} else {
  if (dim > 0) {
    for (let i = 0; i < dim; i++) {
      let row = '';
      for (let j = 0; j < dim; j++) {
        row += 'X';
      }
      console.log(row + '');
    }
  }
}
