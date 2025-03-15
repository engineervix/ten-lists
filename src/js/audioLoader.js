import config from './config.js'

// This class manages loading audio files and handles errors
export class AudioLoader {
  constructor() {
    this.cache = new Map() // Cache for audio file availability checks
    this.retryCount = 3 // Number of retries for failed loads
    this.retryDelay = 1000 // Milliseconds to wait between retries
  }

  // Check if an audio file is available at the given URL
  async checkFileAvailability(url) {
    // Return from cache if we've already checked this URL
    if (this.cache.has(url)) {
      return this.cache.get(url)
    }

    // Perform a HEAD request to check if the file exists
    try {
      const response = await fetch(url, { method: 'HEAD' })
      const isAvailable = response.ok
      this.cache.set(url, isAvailable) // Store in cache
      return isAvailable
    } catch (error) {
      console.error(`Error checking file availability: ${url}`, error)
      this.cache.set(url, false) // Cache negative result
      return false
    }
  }

  // Get a readable error message for the user when a file isn't available
  getErrorMessage(url) {
    if (config.isDevelopment) {
      return `Audio file not found in local development: ${url}`
    } else {
      return `Audio file not available from storage. Please try again later.`
    }
  }

  // Load an audio file with retries and error handling
  async loadAudioWithRetry(url, player) {
    let attempts = 0

    while (attempts < this.retryCount) {
      try {
        // Check if file exists before trying to play
        const isAvailable = await this.checkFileAvailability(url)

        if (!isAvailable) {
          throw new Error(`File not available: ${url}`)
        }

        // Set the player source
        player.source = {
          type: 'audio',
          sources: [
            {
              src: url,
              type: 'audio/mp3',
            },
          ],
        }

        return true // Success
      } catch (error) {
        attempts++
        console.warn(`Attempt ${attempts} failed to load audio: ${url}`, error)

        if (attempts < this.retryCount) {
          // Wait before retrying
          await new Promise((resolve) => setTimeout(resolve, this.retryDelay))
        }
      }
    }

    // If we get here, all attempts failed
    console.error(`Failed to load audio after ${this.retryCount} attempts: ${url}`)
    return false
  }
}

// Create and export a singleton instance
export const audioLoader = new AudioLoader()
