$(function(){
  $("#header").load("items/header.html");
  $("#footer").load("items/footer.html");
  $("#dark_theme_toggle").load("items/dark_theme_toggle.html");
});

function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-theme");
}