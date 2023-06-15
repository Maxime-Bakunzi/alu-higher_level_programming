#!/usr/bin/node
const arg = process.argv[2];

if (!arg || isNaN(arg)) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);

  if (size <= 0) {
    console.log('Invalid size');
  } else {
    const row = 'X'.repeat(size);

    for (let i = 0; i < size; i++) {
      console.log(row);
    }
  }
}
