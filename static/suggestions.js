function suggestion_item_over(suggestion) {
   suggestion.style.backgroundColor = 'yellow';
}

function suggestion_item_onclick(suggestion, number) {
   window.location = "./" + number;
}

function suggestion_item_out(suggestion) {
   suggestion.style.backgroundColor = 'white';
}
