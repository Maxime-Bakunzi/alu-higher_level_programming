#!/usr/bin/node
const argument1 = process.argv[2];
const argument2 = process.argv[3];

if (typeof argument1 === 'undefined' || typeof argument2 === 'undefined') {
  console.log("Insufficient arguments");
} else {
  console.log(argument1 + " is " + argument2);
}

