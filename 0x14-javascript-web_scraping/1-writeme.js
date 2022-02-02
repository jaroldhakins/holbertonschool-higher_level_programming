#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const texto = process.argv[3];

fs.writeFile(file, texto, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
