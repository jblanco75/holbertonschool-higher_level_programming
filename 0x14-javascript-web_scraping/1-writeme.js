#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs');

fs.writefile(process.argv[2], 'utf8', (err, data) => {
  return err ? console.log(err) : console.log(data);
});
