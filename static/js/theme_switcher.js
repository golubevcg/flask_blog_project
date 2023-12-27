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
        document.body.classList.add("light-theme");
    } else {
        document.body.classList.remove("light-theme");
    }
}
