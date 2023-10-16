#!/usr/bin/node

const firstArg = Math.floor(Number(process.argv[2]));
console.log(!isNaN(firstArg) ? `My number: ${firstArg}` : 'Not a number');
