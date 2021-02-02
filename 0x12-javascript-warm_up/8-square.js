#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
}
for (let i = 1; i <= parseInt(process.argv[2]); i++) {
  console.log('X'.repeat(parseInt(process.argv[2])));
}
