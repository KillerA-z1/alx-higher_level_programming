#!/usr/bin/node

const fs = require('fs');
const [file] = process.argv.slice(2);

fs.readFile(file, 'utf-8', (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
