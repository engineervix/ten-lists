import Alpine from 'alpinejs'
import Plyr from 'plyr'
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'
import Swal from 'sweetalert2'
import { audioLoader } from './audioLoader.js'
import { themeManager } from './themeManager.js'
import 'plyr/dist/plyr.css'
import '@phosphor-icons/web/regular'
import '@phosphor-icons/web/fill'
import 'sweetalert2/dist/sweetalert2.min.css'
import '../css/main.css'

// Import our main application logic
import { generateReadingPlan } from './main.js'
import config from './config.js'

// Configure dayjs with relative time plugin
dayjs.extend(relativeTime)

// Make Alpine available globally
window.Alpine = Alpine

// Initialize the theme manager
document.addEventListener('DOMContentLoaded', () => {
  themeManager.init()
})

// Initialize Alpine.js component for the app
document.addEventListener('DOMContentLoaded', () => {
  // Define the Alpine component
  Alpine.data('tenlistsApp', () => ({
    currentDay: 1,
    dayPickerValue: 1,
    showDayPicker: false,
    readings: [],
    currentReadingIndex: 0,
    player: null,
    isLoading: false,
    isPlaying: false,
    loadingTrack: false,
    playerInitialized: false,
    isMobile: window.innerWidth < 768, // Track if we're on mobile
    buildTime: null,

    // Theme management
    isDarkTheme() {
      return themeManager.isDarkTheme()
    },

    toggleTheme() {
      const newTheme = themeManager.toggleTheme()

      // Update SweetAlert2 theme to match the app theme
      if (this.playerInitialized) {
        this.updateSweetAlertTheme(newTheme)
      }

      return newTheme
    },

    // Update SweetAlert2 theme
    updateSweetAlertTheme(theme) {
      // Configure SweetAlert2 to match the current theme
      const isDark = theme === themeManager.THEMES.DARK

      Swal.mixin({
        background: isDark ? 'hsl(var(--b1))' : 'hsl(var(--b1))',
        color: isDark ? 'hsl(var(--bc))' : 'hsl(var(--bc))',
        confirmButtonColor: 'hsl(var(--p))',
      })
    },

    init() {
      // No need to fetch build time, it's now injected at build time

      // Try to load the last day from local storage
      const savedDay = localStorage.getItem('tenlistsCurrentDay')
      if (savedDay) {
        this.currentDay = parseInt(savedDay)
        this.dayPickerValue = parseInt(savedDay)
      }

      // Generate readings first
      this.updateReadings()

      // Initialize Plyr when Alpine component is initialized
      this.$nextTick(() => {
        this.initPlayer()
      })

      // Set up theme update observer
      this.observeThemeChanges()

      // Listen for resize events to update mobile status
      window.addEventListener('resize', () => {
        this.isMobile = window.innerWidth < 768
        // Re-initialize player with appropriate options when screen size changes
        if (this.player) {
          const currentTime = this.player.currentTime
          const wasPlaying = this.isPlaying
          this.player.destroy()
          this.initPlayer()
          this.player.currentTime = currentTime
          if (wasPlaying) {
            this.player.play()
          }
        }
      })

      // Initialize SweetAlert2 theme
      this.updateSweetAlertTheme(themeManager.getCurrentTheme())
    },

    // Setup observer for theme changes to update components
    observeThemeChanges() {
      // Use MutationObserver to watch for theme attribute changes on html element
      const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.type === 'attributes' && mutation.attributeName === 'data-theme') {
            // Update SweetAlert theme when data-theme changes
            this.updateSweetAlertTheme(themeManager.getCurrentTheme())
          }
        })
      })

      // Start observing
      observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['data-theme'],
      })
    },

    // Get relative time since last rebuild
    getLastRebuiltText() {
      const buildTime = config.buildInfo.getBuildTime()
      return buildTime ? dayjs(buildTime).fromNow() : 'recently'
    },

    initPlayer() {
      const element = document.getElementById('player')
      if (element) {
        // Define controls based on device type
        const controlsToShow = this.isMobile
          ? [
              'play', // Play/pause playback
              'current-time', // The current time of playback
              'progress', // The progress bar and scrubber for playback and buffering
              'duration', // The full duration of the media
              'mute', // Toggle mute
              'volume', // Volume control
              'settings', // Settings menu
            ]
          : [
              'play-large', // The large play button in the center
              'restart', // Restart playback
              'rewind', // Rewind by the seek time (default 10 seconds)
              'play', // Play/pause playback
              'fast-forward', // Fast forward by the seek time (default 10 seconds)
              'progress', // The progress bar and scrubber for playback and buffering
              'current-time', // The current time of playback
              'duration', // The full duration of the media
              'mute', // Toggle mute
              'volume', // Volume control
              'settings', // Settings menu
              'airplay', // Airplay (currently Safari only)
            ]

        // Initialize the player with optimized settings
        this.player = new Plyr(element, {
          controls: controlsToShow,
          keyboard: { focused: true, global: true },
          seekTime: 10,
          toggleInvert: false,
          tooltips: { controls: true, seek: true },
          muted: false,
          hideControls: false,
          fullscreen: { enabled: false }, // We don't need fullscreen for audio
          speed: { selected: 1, options: [0.5, 0.75, 1, 1.25, 1.5, 1.75, 2] },
          invertTime: true,
          // Optimize for touch on mobile
          touchControls: this.isMobile ? 'auto' : false,
        })

        // Mark player as initialized
        this.playerInitialized = true

        // Set up event listeners
        this.player.on('ended', () => {
          this.playNext()
        })

        // Add listener for play/pause events for better sync
        this.player.on('play', () => {
          this.isPlaying = true
        })

        this.player.on('pause', () => {
          this.isPlaying = false
        })

        // Add listener for when src changes
        this.player.on('loadeddata', () => {
          // Ensure UI is updated when a new track is loaded
          this.$nextTick(() => {
            // Make sure we highlight the correct item in the reading list
            this.highlightCurrentReading()
            this.loadingTrack = false
          })
        })

        // After player is initialized, update the source
        this.updatePlayerSource()
      }
    },

    updateReadings() {
      this.isLoading = true

      // Pause any currently playing audio before changing readings
      if (this.player && this.isPlaying) {
        this.player.pause()
        this.isPlaying = false
      }

      this.readings = generateReadingPlan(this.currentDay)
      this.currentReadingIndex = 0
      this.isLoading = false

      // Save current day to local storage
      localStorage.setItem('tenlistsCurrentDay', this.currentDay.toString())

      // Only update player source if player is already initialized
      if (this.playerInitialized && this.player) {
        this.updatePlayerSource()
      }
    },

    updatePlayerSource() {
      // Make sure player is initialized and readings are available
      if (!this.playerInitialized || !this.player || this.readings.length === 0) {
        return
      }

      // Show loading indicator
      this.loadingTrack = true

      // Get current reading
      const currentReading = this.readings[this.currentReadingIndex]

      if (!currentReading) {
        console.error('No reading found for index:', this.currentReadingIndex)
        this.loadingTrack = false
        return
      }

      // Use the AudioLoader to handle loading with retries and error handling
      audioLoader
        .loadAudioWithRetry(currentReading.filePath, this.player)
        .then((success) => {
          if (!success) {
            // Handle the case where audio couldn't be loaded
            this.handleAudioLoadError(currentReading)
          } else {
            // Scroll the current reading into view in the list
            this.$nextTick(() => {
              this.highlightCurrentReading()
            })
          }
        })
        .catch((error) => {
          console.error('Error updating player source:', error)
          this.handleAudioLoadError(currentReading)
        })
        .finally(() => {
          this.loadingTrack = false
        })
    },

    handleAudioLoadError(reading) {
      const errorMessage = audioLoader.getErrorMessage(reading.filePath)

      // Use SweetAlert2 with theme-aware options
      const isDark = themeManager.isDarkTheme()

      Swal.fire({
        title: 'Audio Error',
        text: `Unable to load audio for ${reading.reference}. ${errorMessage}`,
        icon: 'error',
        confirmButtonText: 'OK',
        confirmButtonColor: 'hsl(var(--p))',
        background: isDark ? 'hsl(var(--b1))' : 'hsl(var(--b1))',
        color: isDark ? 'hsl(var(--bc))' : 'hsl(var(--bc))',
      })

      // Optionally, you could try loading the next track automatically
      // if (this.currentReadingIndex < this.readings.length - 1) {
      //   this.currentReadingIndex++;
      //   this.updatePlayerSource();
      // }
    },

    highlightCurrentReading() {
      // Find the active reading item and scroll it into view
      const activeItem = document.querySelector(
        `.reading-item[data-index="${this.currentReadingIndex}"]`
      )
      if (activeItem) {
        activeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
      }
    },

    playReading(index) {
      if (index >= 0 && index < this.readings.length) {
        if (index === this.currentReadingIndex && this.isPlaying) {
          // If clicking the current track and it's playing, pause it
          this.player.pause()
        } else {
          // Otherwise, play the selected track
          this.currentReadingIndex = index
          this.updatePlayerSource()

          // Wait for source to be loaded before playing
          setTimeout(() => {
            if (this.player) {
              this.player.play().catch((error) => {
                console.error('Error playing audio:', error)
              })
            }
          }, 100)
        }
      }
    },

    playNext() {
      if (this.currentReadingIndex < this.readings.length - 1) {
        this.currentReadingIndex++
        this.updatePlayerSource()

        // Wait for source to be loaded before playing
        setTimeout(() => {
          if (this.player) {
            this.player.play().catch((error) => {
              console.error('Error playing next track:', error)
            })
          }
        }, 100)
      }
    },

    playPrevious() {
      if (this.currentReadingIndex > 0) {
        this.currentReadingIndex--
        this.updatePlayerSource()

        // Wait for source to be loaded before playing
        setTimeout(() => {
          if (this.player) {
            this.player.play().catch((error) => {
              console.error('Error playing previous track:', error)
            })
          }
        }, 100)
      }
    },

    setDay(day) {
      if (day >= 1) {
        // Pause any currently playing audio
        if (this.player && this.isPlaying) {
          this.player.pause()
          this.isPlaying = false
        }

        this.currentDay = parseInt(day)
        this.dayPickerValue = parseInt(day)
        this.updateReadings()
      }
    },

    incrementDay() {
      this.setDay(this.currentDay + 1)
    },

    decrementDay() {
      if (this.currentDay > 1) {
        this.setDay(this.currentDay - 1)
      }
    },

    getCurrentReading() {
      return this.readings[this.currentReadingIndex] || null
    },
  }))

  // Start Alpine
  Alpine.start()
})

// After the page loads, initialize BLB ScriptTagger
window.addEventListener('DOMContentLoaded', () => {
  // Initialize BLB ScriptTagger configuration
  window.BLB = window.BLB || {}
  window.BLB.Tagger = window.BLB.Tagger || {}

  BLB.Tagger.Translation = 'ESV'
  BLB.Tagger.HyperLinks = 'all'
  BLB.Tagger.HideTags = false
  BLB.Tagger.TargetNewWindow = true
  BLB.Tagger.Style = 'par'
  BLB.Tagger.NoSearchTagNames = ''
  BLB.Tagger.NoSearchClassNames = 'noTag doNotTag'

  // Initialize tagging
  if (typeof BLB !== 'undefined' && BLB.Tagger && BLB.Tagger.tag) {
    BLB.Tagger.tag()
  }
})
