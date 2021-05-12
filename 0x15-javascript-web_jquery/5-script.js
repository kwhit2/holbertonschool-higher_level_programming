// JavaScript script that adds a <li> element to a list when the user clicks
// on the tag DIV#add_item:
// 1. The new element must be: <li>Item</li>
// 2. The new element must be added to UL.my_list
// 3. can’t use document.querySelector to select the HTML tag
// 4. must use the JQuery API
$('#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
