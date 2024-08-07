/* global $ */
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      const movies = data.results;
      for (const movie of movies) {
        $('<li></li>').text(movie.title).appendTo('#list_movies');
      }
    },
    error: function (error) {
      console.error('Error fetching data:', error);
    }
  });
});
