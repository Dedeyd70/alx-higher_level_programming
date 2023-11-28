#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request.get(URL, function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
