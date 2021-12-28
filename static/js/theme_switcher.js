// theme update function called when theme switcher clicked
function switch_theme() {
    let switch_state = document.getElementById("theme-switcher-checkbox").checked;
    let updated_theme = "light"
    if (switch_state) {
        updated_theme = "dark"
    }
    localStorage["theme"] =  updated_theme;
    let element = document.body;
    element.classList.toggle("dark-theme");

}

// set checked state based on current theme in local storage
$( document ).ready(function() {
  if (storageAvailable('localStorage')) {
    let theme = localStorage["theme"]
    if(theme && theme === "dark" || !!!theme) {
      document.getElementById("theme-switcher-checkbox").checked = true;
      switch_theme()
    }
  }
});

function storageAvailable(type) {
	try {
		let storage = window[type],
			x = '__storage_test__';
		storage.setItem(x, x);
		storage.removeItem(x);
		return true;
	}
	catch(e) {
		return false;
	}
}