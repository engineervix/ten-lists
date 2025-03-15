// Environment configuration for the application
// Detects whether we're in development or production mode and sets appropriate paths

// Determine the environment
const isDevelopment = typeof import.meta.env !== 'undefined' ? import.meta.env.DEV : true
const isProduction = typeof import.meta.env !== 'undefined' ? import.meta.env.PROD : false

// Storage configuration
const storage = {
  // Get the base URL for audio files from environment variables
  // Default to "/audio" for local development if not specified
  baseUrl:
    typeof import.meta.env !== 'undefined'
      ? import.meta.env.VITE_MP3_BASE_URL || '/audio'
      : '/audio',

  // Simple getter for the base URL (keeping the function for API compatibility)
  getBaseUrl() {
    return this.baseUrl
  },
}

// Build information
const buildInfo = {
  // Getter for build time
  getBuildTime() {
    return __BUILD_DATE__
  },
}

// App configuration
const config = {
  isDevelopment,
  isProduction,
  storage,
  buildInfo,
}

export default config
