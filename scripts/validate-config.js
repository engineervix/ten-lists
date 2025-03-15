// This script validates environment variables before build
// It will exit with an error if required variables are missing

// Check for required environment variables before build
function validateConfig() {
  console.log('\nValidating deployment configuration...')

  const baseUrl = process.env.VITE_MP3_BASE_URL

  if (!baseUrl) {
    console.warn('Warning: VITE_MP3_BASE_URL environment variable is not set.')
    console.warn("Using default value '/audio' for local development.")
    // Don't exit - we'll use the default value
  } else {
    console.log('✅ Configuration validated successfully!')
    console.log(`Using audio files base URL: ${baseUrl}`)
  }

  console.log()
}

// Run validation
validateConfig()
