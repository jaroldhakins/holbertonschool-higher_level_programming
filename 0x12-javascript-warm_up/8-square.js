#!/usr/bin/node
const cadena = process.argv.slice(2);
const num = Number(cadena[0]);
const comp = isNaN(num);
let x;
if (comp === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    x = '';
    for (let j = 0; j < num; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
