#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    characterUrls.forEach((characterUrl) => {
      request.get(characterUrl, (charErr, charResponse, charBody) => {
        if (charErr) {
          console.error(charErr);
        } else if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.error(`Error: ${charResponse.statusCode}`);
        }
      });
    });
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
