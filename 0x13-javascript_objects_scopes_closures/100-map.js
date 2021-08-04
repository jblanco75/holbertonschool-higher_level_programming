#!/usr/bin/node

const list = require('./100-data');
const list1 = require('./100-data').list;
const list2 = list1.map((index, value) => index * value);
console.log(list1);
console.log(list2);
