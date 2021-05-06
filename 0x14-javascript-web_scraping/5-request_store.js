#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);

request.get(args[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(args[1], body);
  }
});
