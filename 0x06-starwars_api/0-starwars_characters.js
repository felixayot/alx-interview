#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');
async function getCharacters (movieId) {
  try {
    const response = await request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const characters = response.data.characters;
    for (const characterUrl of characters) {
      const characterResponse = await request.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

const movieId = process.argv[2];
getCharacters(movieId);
