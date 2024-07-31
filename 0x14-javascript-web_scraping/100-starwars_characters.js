#!/usr/bin/node

const request = require('request');

const [movieId] = process.argv.slice(2);
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

function fetchMovieCharacters () { // Added space before function parentheses
  request(`${apiUrl}${movieId}`, (error, response, body) => {
    if (error) {
      return console.error(error);
    }
    const characterUrls = JSON.parse(body).characters;
    for (const characterUrl of characterUrls) {
      request(characterUrl, (error, response, body) => {
        if (error) {
          return console.error(error);
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    }
  });
}

fetchMovieCharacters();
