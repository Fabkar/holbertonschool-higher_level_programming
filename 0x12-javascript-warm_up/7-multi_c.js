#!/usr/bin/node
/* console.log('C is fun\n'.repeat(parseInt(process.argv[2]))); */
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
for (let i = 1; i <= parseInt(process.argv[2]); i++) {
  console.log('C is fun');
}
