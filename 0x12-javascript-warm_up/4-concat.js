#!/usr/bin/node
const cadena = process.argv.slice(2);
if (cadena[0] === undefined && cadena[1] === undefined) {
  console.log('undefined is undefined');
} else if (cadena[0] !== undefined && cadena[1] !== undefined) {
  console.log(cadena[0] + ' is ' + cadena[1]);
} else if (cadena[0] !== undefined && cadena[1] === undefined) {
  console.log(cadena[0] + ' is undefined');
} else if (cadena[0] === undefined && cadena[1] !== undefined) {
  console.log('undefined is ' + cadena[1]);
}
