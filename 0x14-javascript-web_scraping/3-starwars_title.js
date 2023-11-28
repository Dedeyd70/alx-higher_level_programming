#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const movieData = JSON.parse(body);
  if (movieData.detail === 'Not found') {
    console.log(`Err: Movie with ID ${movieID} not found.`);
    return;
  }
  console.log(`${movieData.title}`);
});
