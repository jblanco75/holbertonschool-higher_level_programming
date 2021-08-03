#!/usr/bin/node

const arr1 = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 1; i < process.argv.length; i++) {
    arr1.push(parseInt(process.argv[i]));
  }
  console.log(
    arr1.sort((a, b) => {
      return a - b;
    })[arr1.length - 2]
  );
}
