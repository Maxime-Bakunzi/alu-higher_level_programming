#!/usr/bin/node
const argument = process.argv[2];

const convertedNumber = parseInt(argument, 10);

if (!isNaN(convertedNumber)) {
  console.log('My number: ' + convertedNumber);
} else {
  console.log('Not a number');
}
