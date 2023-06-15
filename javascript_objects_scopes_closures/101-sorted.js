#!/usr/bin/node

const data = require('./101-data').dict;

const sortedDict = {};

for (const userId in data) {
  const occurrences = data[userId];
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(userId.toString());
}

console.log(sortedDict);
