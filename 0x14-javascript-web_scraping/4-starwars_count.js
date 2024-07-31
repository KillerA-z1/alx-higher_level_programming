#!/usr/bin/node

const request = require('request');

const [apiUrl] = process.argv.slice(2);

function countCharactersWithId () { // Added space before function parentheses
  request(apiUrl, (error, response, body) => {
    if (error) {
      return console.error(error);
    }
    const data = JSON.parse(body);
    let count = 0;
    for (const film of data.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  });
}

countCharactersWithId();
