#!/usr/bin/node
const argt = process.argv.slice(2);
const mynumber = Number(argt[0]);
const x = isNaN(mynumber);
if (x === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + mynumber);
}
