#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', err => {
  if (err) {
    console.log(err);
  }
});
