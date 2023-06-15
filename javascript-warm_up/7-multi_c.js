#!/usr/bin/node
const arg = process.argv[2];

if (!arg || isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  const numOccurrences = parseInt(arg);

  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
