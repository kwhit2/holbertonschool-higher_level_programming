// JavaScript script that fetches and lists the title for all movies by using
// this URL: https://swapi-api.hbtn.io/api/films/?format=json
// 1. All movie titles must be list in the HTML tag UL#list_movies
// 2. must use the JQuery API
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (info) {
  $.each(info.results, function (index, value) {
    $('#list_movies').append(value.title);
  });
});
