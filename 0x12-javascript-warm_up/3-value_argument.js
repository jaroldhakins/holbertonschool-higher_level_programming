#!/usr/bin/node
const cadena = process.argv.slice(2);
if (cadena[0] === undefined) {
  console.log('No argument');
} else {
  console.log(cadena[0]);
}
