function suggestion_item_over(suggestion) {
   suggestion.style.backgroundColor = 'yellow';
}

function suggestion_item_onclick(suggestion, suggestion_number, page_number) {
   window.location = "./" + suggestion_number + "?page=" + page_number;
}

function suggestion_item_out(suggestion) {
   suggestion.style.backgroundColor = 'white';
}
