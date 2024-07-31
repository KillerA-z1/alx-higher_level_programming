#!/usr/bin/node

const fs = require('fs');
const [filePath, fileContent] = process.argv.slice(2);

fs.writeFile(filePath, fileContent, 'utf8', error => {
  if (error) console.error(error);
});
