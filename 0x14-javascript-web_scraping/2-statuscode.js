#!/usr/bin/node

const request = require('request');
const [requestUrl] = process.argv.slice(2);

request(requestUrl, (requestError, requestResponse) => {
  if (requestError) {
    return console.error(requestError);
  }
  console.log(`code: ${requestResponse.statusCode}`);
});
