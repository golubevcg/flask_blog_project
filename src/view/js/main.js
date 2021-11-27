$(function(){
  $("#header").load("header.html");
  $("#footer").load("footer.html");
});

function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-theme");
}