#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2] || 'https://swapi-api.alx-tools.com/api/films/';
const wedgeAntillesID = 18;

request.get(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  try {
    const filmsData = JSON.parse(body);

    if (filmsData && filmsData.results) {
      const moviesWithWedgeAntilles = filmsData.results.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`));

      console.log(`${moviesWithWedgeAntilles.length}`);
    } else {
      console.error('Invalid API response structure');
    }
  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
});

