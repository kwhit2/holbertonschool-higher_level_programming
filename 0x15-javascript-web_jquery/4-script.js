// JavaScript script that toggles the class of the <header> element when the
// user clicks on the tag DIV#toggle_header:
// 1. The <header> element must always have one class: red or green, never
// both in the same time and never empty.
// 2. If the current class is red, when the user click on DIV#toggle_header,
// the class must be updated to green ; and the reverse.
// 3. can’t use document.querySelector to select the HTML tag
// 4. must use the JQuery API
$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
