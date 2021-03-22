#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs[0] && isNaN(myArgs[0]) === false) {
  console.log('My number: ' + parseInt(myArgs[0]));
} else {
  console.log('Not a number');
}
