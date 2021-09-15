#!/usr/bin/node
// Script that prints the number of movies
// where the character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  let count = 0;
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body);
  for (let i = 0; movie.results[i] !== undefined; i++) {
    if (movie.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count += 1;
    }
  }
  console.log(count);
});
