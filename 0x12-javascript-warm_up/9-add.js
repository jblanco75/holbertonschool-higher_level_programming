#!/usr/bin/node

function add (a, b) {
  const number1 = parseInt(process.argv[2]);
  const number2 = parseInt(process.argv[3]);
  if (isNaN(number1) || isNaN(number2)) {
    return NaN;
  } else {
    return number1 + number2;
  }
}
console.log(add(process.argv[2], process.argv[3]));
