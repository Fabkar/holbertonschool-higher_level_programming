#!/usr/bin/node
const argum = process.argv.slice(2).map((x) => parseInt(x));
if (argum.length === 0 || argum.length === 1) console.log(0);
else {
  const maxArg = Math.max(...argum);
  argum.splice(argum.indexOf(maxArg), 1);
  console.log(Math.max(...argum));
}
