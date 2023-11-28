#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];
const wedgeAntillesID = 18;

request.get(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const filmsData = JSON.parse(body);
  const moviesWithWedgeAntilles = filmsData.results.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`));

  console.log(`${moviesWithWedgeAntilles.length}`);
});
