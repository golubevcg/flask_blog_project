// Immediately apply the theme on page load
if (localStorage.getItem("theme") === "light") {
    document.documentElement.classList.add("light-theme");
} else {
    document.documentElement.classList.remove("light-theme");
}

function switch_theme() {
    // Determine the current theme
    let current_theme = localStorage.getItem("theme");

    // If the current theme is 'light', switch to 'dark' (which is defined by :root styles)
    // Otherwise, switch to 'light'
    let updated_theme = (current_theme === "light") ? "dark" : "light";
    
    // Update the theme in localStorage
    localStorage.setItem("theme", updated_theme);

    // Apply the new theme
    if (updated_theme === "light") {
        document.documentElement.classList.add("light-theme");
    } else {
        document.documentElement.classList.remove("light-theme");
    }
}
