#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const cadena = process.argv.slice(2);
const size = cadena.length;
const num1 = Number(cadena[0]);
const num2 = Number(cadena[1]);
if (size < 2) {
  console.log('NaN');
} else {
  const result = add(num1, num2);
  console.log(result);
}
