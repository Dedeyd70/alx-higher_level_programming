#!/usr/bin/node

const firstArg = process.argv[2];
const message = firstArg ? `${firstArg}` : 'No argument';
console.log(message);
