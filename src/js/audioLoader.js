import config from './config.js'

// This class manages loading audio files and handles errors
export class AudioLoader {
  constructor() {
    this.cache = new Map() // Cache for audio file availability checks
    this.retryCount = 3 // Number of retries for failed loads
    this.retryDelay = 1000 // Milliseconds to wait between retries
    this.preloadQueue = [] // Queue for preloading audio files
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

  // Preload an audio file in the background
  async preloadAudio(url) {
    if (this.cache.has(url) && this.cache.get(url) === false) {
      // Skip preloading if we already know the file is not available
      return false
    }

    try {
      // Check if file exists
      const isAvailable = await this.checkFileAvailability(url)

      if (!isAvailable) {
        return false
      }

      // Create a hidden audio element to preload the file
      const preloadAudio = new Audio()
      preloadAudio.src = url
      preloadAudio.preload = 'auto'

      // Set event listeners for debugging
      preloadAudio.addEventListener('canplaythrough', () => {
        console.debug(`Preloaded audio file: ${url}`)
      })

      preloadAudio.addEventListener('error', (e) => {
        console.warn(`Error preloading audio: ${url}`, e)
      })

      // Start loading the audio but don't wait for it to complete
      preloadAudio.load()

      // Store in the preload queue to keep a reference
      this.preloadQueue.push(preloadAudio)

      // Limit the preload queue size
      if (this.preloadQueue.length > 3) {
        this.preloadQueue.shift()
      }

      return true
    } catch (error) {
      console.warn(`Failed to preload audio: ${url}`, error)
      return false
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
