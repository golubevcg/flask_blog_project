function switch_theme() {
  let element = document.body;
  element.classList.toggle("dark-theme");
  localStorage.setItem("theme","dark");
};

let theme = localStorage.getItem("theme")
if (theme && theme === "dark"){
    switch_theme()
}

$( document ).ready(function() {
  if (theme && theme === "dark"){
    document.getElementById("theme-switcher-checkbox").checked = true;
  }
});