#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const [url, outputFilename] = process.argv.slice(2);

function fetchAndSaveData () { // Added space before function parentheses
  request(url, (error, response, body) => {
    if (error) {
      return console.error(error);
    }
    fs.writeFile(outputFilename, body, 'utf8', error => {
      if (error) {
        return console.error(error);
      }
    });
  });
}

fetchAndSaveData();
