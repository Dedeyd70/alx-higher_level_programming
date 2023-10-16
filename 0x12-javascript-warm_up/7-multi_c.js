#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let d = 0; d < x; d++) {
    console.log('C is fun');
  }
}
