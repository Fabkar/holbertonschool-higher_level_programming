#!/usr/bin/node
/*
console.log(process.argv.length === 2 ? 'No argument' : process.argv.length === 3 ? 'Argument found' : 'Arguments found')
*/
if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
