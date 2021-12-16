#!/usr/bin/node
function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const cadena = process.argv.slice(2);
const num = Number(cadena[0]);
if (isNaN(cadena[0])) {
  console.log(1);
} else {
  console.log(factorial(num));
}
