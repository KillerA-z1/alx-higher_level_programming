#!/usr/bin/node

const request = require('request');

const [episodeNumber] = process.argv.slice(2);

function fetchMovieTitle () { // Added space before function parentheses
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
  request(`${apiUrl}${episodeNumber}`, (error, response, body) => {
    if (error) {
      return console.error(error);
    }
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  });
}

fetchMovieTitle();
