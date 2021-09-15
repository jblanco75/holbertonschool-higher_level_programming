#!/usr/bin/node
// Script that prints the number of movies
// where the character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body).results;
    let count = 0;
    for (const mov of movie) {
      for (const character of mov.characters) {
        if (character.includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
