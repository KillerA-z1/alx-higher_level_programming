#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function fetchCharacterNames () { // Added space before function parentheses
  request(apiUrl, (error, response, body) => {
    if (error) {
      return console.error(`Error fetching film data: ${error.message}`);
    }
    try {
      const filmData = JSON.parse(body);
      const characterUrls = filmData.characters;

      characterUrls.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            return console.error(`Error fetching character data: ${error.message}`);
          }
          try {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          } catch (error) {
            console.error(`Error parsing character data: ${error.message}`);
          }
        });
      });
    } catch (error) {
      console.error(`Error parsing film data: ${error.message}`);
    }
  });
}

fetchCharacterNames();
