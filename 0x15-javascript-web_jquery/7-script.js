// JavaScript script that fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
// 1. name must be displayed in the HTML tag DIV#character
// 2. must use the JQuery API
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (info) {
  $('#character').append(info.name);
});
