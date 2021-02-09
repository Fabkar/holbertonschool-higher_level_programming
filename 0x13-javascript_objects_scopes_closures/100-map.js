#!/usr/bin/node
/* script that imports an array and computes a new array. */
const list = require('./100-data.js').list;
console.log(list);
const nlist = list.map((x, index) => x * index);
console.log(nlist);
