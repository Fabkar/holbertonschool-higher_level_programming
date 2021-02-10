#!/usr/bin/node
/* script that writes a string to a file */
const fs = require('fs'); // Requiring fs module in which readFile function id defined.
const content = process.argv[3]; // argument is the string to write.

fs.writeFile(process.argv[2], content, err => {
  if (err) { console.error(err); }
});
