// This script runs after the build to perform any final tasks
// Such as preparing files for deployment or generating reports
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

// Get the directory name
const __dirname = path.dirname(fileURLToPath(import.meta.url))
const distDir = path.resolve(__dirname, '../dist')

function run() {
  console.log('\nRunning post-build operations...')

  // Create a _headers file for Cloudflare Pages (if you're using it)
  createCloudflareHeaders()

  console.log('✅ Post-build operations completed!\n')
}

// Create a _headers file for Cloudflare Pages
// This sets caching headers and security policies
function createCloudflareHeaders() {
  const headersPath = path.join(distDir, '_headers')
  const headers = `# Cloudflare Headers
/*
  Cache-Control: public, max-age=86400
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

# Cache audio files longer
/audio/*
  Cache-Control: public, max-age=2592000, immutable

# Cache assets
/assets/*
  Cache-Control: public, max-age=31536000, immutable
`

  fs.writeFileSync(headersPath, headers)
  console.log('Created Cloudflare _headers file')
}

// Run the script
run()
