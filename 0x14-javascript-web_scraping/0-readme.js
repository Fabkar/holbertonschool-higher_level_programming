#!/usr/bin/node
/* script that reads and prints the content of a file. */
const fs = require('fs'); // Requiring fs module in which readFile function id defined.

fs.readFile(process.argv[2], 'utf-8', (err, data) => { // Reading data in utf8 format
  if (err) { console.log(err); }

  console.log(data);
});
