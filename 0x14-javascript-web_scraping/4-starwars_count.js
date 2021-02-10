#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present */
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let n = 0;
    for (const film of films) {
      for (const char of film.characters) {
        if (char.includes('18')) {
          n++;
          break;
        }
      }
    }
    console.log(n);
  }
});
