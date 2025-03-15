export const themeManager = {
  // Theme constants
  THEMES: {
    LIGHT: 'winter',
    DARK: 'night',
  },

  // Storage key for theme preference
  STORAGE_KEY: 'tenlists-bible-theme',

  // Initialize theme based on user preference or system preference
  init() {
    // Check if user has previously saved a theme preference
    const savedTheme = localStorage.getItem(this.STORAGE_KEY)

    if (savedTheme) {
      // Apply saved theme
      this.setTheme(savedTheme)
    } else {
      // Check for system preference
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
      this.setTheme(prefersDark ? this.THEMES.DARK : this.THEMES.LIGHT)
    }

    // Add listener for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      // Only apply if user hasn't manually set a preference
      if (!localStorage.getItem(this.STORAGE_KEY)) {
        this.setTheme(e.matches ? this.THEMES.DARK : this.THEMES.LIGHT)
      }
    })
  },

  // Toggle between light and dark themes
  toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme')
    const newTheme = currentTheme === this.THEMES.LIGHT ? this.THEMES.DARK : this.THEMES.LIGHT
    this.setTheme(newTheme)
    return newTheme
  },

  // Set a specific theme
  setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem(this.STORAGE_KEY, theme)
    return theme
  },

  // Get current theme
  getCurrentTheme() {
    return document.documentElement.getAttribute('data-theme') || this.THEMES.LIGHT
  },

  // Check if the current theme is dark
  isDarkTheme() {
    return this.getCurrentTheme() === this.THEMES.DARK
  },
}

export default themeManager
