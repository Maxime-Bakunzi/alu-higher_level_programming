$(document).ready(function () {
  $('#add_item').click(function () {
    const listItem = $('<li>').text('Item');
    $('.my_list').append(listItem);
  });
});
