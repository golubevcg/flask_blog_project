// Theme update function called when theme switcher clicked
function switch_theme() {
    // Determine the current theme
    let current_theme = localStorage.getItem("theme");
    // Toggle the theme between 'light' and 'dark'
    let updated_theme = (current_theme === "dark") ? "light" : "dark";
    
    // Update the theme in localStorage
    localStorage.setItem("theme", updated_theme);
    
    // Apply the new theme
    document.body.classList.toggle("dark-theme", updated_theme === "dark");
    console.log("This will be printed to the console");
}
