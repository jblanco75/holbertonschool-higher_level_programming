#!/usr/bin/node

function factorial (n) {
  let answer = 1;
  if (n === 0 || n === 1) {
    return answer;
  } else {
    for (let i = n; i >= 1; i--) {
      answer *= i;
    }
    return answer;
  }
}
console.log(factorial(process.argv[2]));
