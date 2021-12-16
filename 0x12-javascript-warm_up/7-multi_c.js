#!/usr/bin/node
let num;
const cadena = process.argv.slice(2);
if (cadena[0] === undefined) {
  console.log('Missing number of occurrences');
} else {
  num = Number(cadena[0]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
