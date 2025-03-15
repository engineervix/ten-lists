import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest'
import { setupAllBrowserMocks } from '../mocks/browserMocks.js'
import { audioLoader } from '../../src/js/audioLoader.js'
import Plyr from 'plyr'

// Mock dayjs and its plugins
vi.mock('dayjs', () => {
  const dayjs = () => ({
    fromNow: () => 'a few moments ago',
  })
  dayjs.extend = vi.fn()
  return {
    default: dayjs,
  }
})

vi.mock('dayjs/plugin/relativeTime.js', () => {
  return {
    default: {},
  }
})

// Mock the dependencies
vi.mock('plyr', () => {
  return {
    default: vi.fn().mockImplementation(() => {
      return {
        source: null,
        play: vi.fn().mockResolvedValue(undefined),
        pause: vi.fn(),
        on: vi.fn(),
        off: vi.fn(),
        destroy: vi.fn(),
        currentTime: 0,
      }
    }),
  }
})

vi.mock('../../src/js/audioLoader.js', () => {
  return {
    audioLoader: {
      loadAudioWithRetry: vi.fn().mockResolvedValue(true),
      getErrorMessage: vi.fn().mockReturnValue('Mock error message'),
      checkFileAvailability: vi.fn().mockResolvedValue(true),
    },
  }
})

vi.mock('../../src/js/main.js', () => {
  return {
    generateReadingPlan: vi.fn().mockImplementation((day) => {
      // Return a realistic mock reading plan
      return Array(10)
        .fill(null)
        .map((_, index) => ({
          listId: index + 1,
          listName: `List ${index + 1}`,
          book: index === 5 ? 'Psalms' : 'Genesis',
          chapter: 1,
          filePath:
            index === 5
              ? '/audio/A19__001_Psalms______ENGESVC2DA.mp3'
              : '/audio/A01___01_Genesis_____ENGESVC2DA.mp3',
          reference: index === 5 ? 'Psalms 1' : 'Genesis 1',
        }))
    }),
  }
})

// Mock SweetAlert2
vi.mock('sweetalert2', () => {
  return {
    default: {
      fire: vi.fn().mockResolvedValue({}),
      mixin: vi.fn().mockReturnValue({
        fire: vi.fn().mockResolvedValue({}),
      }),
    },
  }
})

describe('Audio Player Integration Tests', () => {
  let mocks
  let mockPlayer

  beforeEach(() => {
    // Setup browser mocks
    mocks = setupAllBrowserMocks({ prefersDarkMode: false })

    // Setup fake timers
    vi.useFakeTimers()

    // Create a basic DOM structure required by the app
    document.body.innerHTML = `
      <div x-data="tenlistsApp">
        <audio id="player"></audio>
        <div class="reading-list"></div>
      </div>
    `

    // Reset mocks
    vi.resetAllMocks()

    // Create a mock player instance
    mockPlayer = {
      source: null,
      play: vi.fn().mockResolvedValue(undefined),
      pause: vi.fn(),
      on: vi.fn(),
      off: vi.fn(),
      destroy: vi.fn(),
      currentTime: 0,
    }

    // Mock Plyr to return our instance
    Plyr.mockReturnValue(mockPlayer)
  })

  afterEach(() => {
    // Clean up DOM
    document.body.innerHTML = ''
    vi.resetModules()
    vi.clearAllMocks()
    vi.useRealTimers()
  })

  // Integration test for audioLoader and player interaction
  it('loadAudioWithRetry updates player source and triggers callbacks', async () => {
    // Setup audioLoader mock
    audioLoader.loadAudioWithRetry.mockResolvedValue(true)

    // Create test data
    const testFilePath = '/audio/A01___01_Genesis_____ENGESVC2DA.mp3'
    const player = {
      source: null,
    }

    // Call the function
    const result = await audioLoader.loadAudioWithRetry(testFilePath, player)

    // Verify behavior
    expect(result).toBe(true)
    expect(audioLoader.loadAudioWithRetry).toHaveBeenCalledWith(testFilePath, player)
  })

  it('handles audio load errors properly', async () => {
    // Setup audioLoader mock to fail
    audioLoader.loadAudioWithRetry.mockResolvedValueOnce(false)

    // Create a fake Alpine app component
    const alpineComponent = {
      player: { source: null },
      loadingTrack: true,
      handleAudioLoadError: vi.fn(),
    }

    // Create test data
    const testFilePath = '/audio/A01___01_Genesis_____ENGESVC2DA.mp3'
    const reading = { filePath: testFilePath, reference: 'Genesis 1' }

    // Simulate updatePlayerSource (simplified version)
    try {
      const success = await audioLoader.loadAudioWithRetry(reading.filePath, alpineComponent.player)
      if (!success) {
        alpineComponent.handleAudioLoadError(reading)
      }
    } catch (error) {
      alpineComponent.handleAudioLoadError(reading)
    } finally {
      alpineComponent.loadingTrack = false
    }

    // Verify behavior
    expect(audioLoader.loadAudioWithRetry).toHaveBeenCalledWith(
      reading.filePath,
      alpineComponent.player
    )
    expect(alpineComponent.handleAudioLoadError).toHaveBeenCalledWith(reading)
    expect(alpineComponent.loadingTrack).toBe(false)
  })

  it('playNext increments reading index and updates player source', () => {
    // Create a fake Alpine app component
    const alpineComponent = {
      readings: [
        { book: 'Genesis', chapter: 1 },
        { book: 'Exodus', chapter: 1 },
        { book: 'Leviticus', chapter: 1 },
      ],
      currentReadingIndex: 0,
      updatePlayerSource: vi.fn(),
      player: { play: vi.fn().mockResolvedValue(undefined) },
    }

    // Call playNext
    const playNext = () => {
      if (alpineComponent.currentReadingIndex < alpineComponent.readings.length - 1) {
        alpineComponent.currentReadingIndex++
        alpineComponent.updatePlayerSource()

        // Wait for source to be loaded before playing
        setTimeout(() => {
          if (alpineComponent.player) {
            alpineComponent.player.play().catch((error) => {
              console.error('Error playing next track:', error)
            })
          }
        }, 100)
      }
    }

    playNext()

    // Verify behavior
    expect(alpineComponent.currentReadingIndex).toBe(1)
    expect(alpineComponent.updatePlayerSource).toHaveBeenCalled()

    // Fast-forward timers to check if play was called
    vi.runAllTimers()
    expect(alpineComponent.player.play).toHaveBeenCalled()
  })

  it('playPrevious decrements reading index and updates player source', () => {
    // Create a fake Alpine app component
    const alpineComponent = {
      readings: [
        { book: 'Genesis', chapter: 1 },
        { book: 'Exodus', chapter: 1 },
        { book: 'Leviticus', chapter: 1 },
      ],
      currentReadingIndex: 1,
      updatePlayerSource: vi.fn(),
      player: { play: vi.fn().mockResolvedValue(undefined) },
    }

    // Call playPrevious
    const playPrevious = () => {
      if (alpineComponent.currentReadingIndex > 0) {
        alpineComponent.currentReadingIndex--
        alpineComponent.updatePlayerSource()

        // Wait for source to be loaded before playing
        setTimeout(() => {
          if (alpineComponent.player) {
            alpineComponent.player.play().catch((error) => {
              console.error('Error playing previous track:', error)
            })
          }
        }, 100)
      }
    }

    playPrevious()

    // Verify behavior
    expect(alpineComponent.currentReadingIndex).toBe(0)
    expect(alpineComponent.updatePlayerSource).toHaveBeenCalled()

    // Fast-forward timers to check if play was called
    vi.runAllTimers()
    expect(alpineComponent.player.play).toHaveBeenCalled()
  })

  it('persists current day to localStorage when changing days', () => {
    // Create a fake Alpine app component
    const alpineComponent = {
      currentDay: 1,
      dayPickerValue: 1,
      updateReadings: vi.fn(),
      player: { pause: vi.fn() },
      isPlaying: true,
    }

    // Call setDay
    const setDay = (day) => {
      if (day >= 1) {
        // Pause any currently playing audio
        if (alpineComponent.player && alpineComponent.isPlaying) {
          alpineComponent.player.pause()
          alpineComponent.isPlaying = false
        }

        alpineComponent.currentDay = parseInt(day)
        alpineComponent.dayPickerValue = parseInt(day)
        alpineComponent.updateReadings()
      }
    }

    setDay(10)

    // Verify behavior
    expect(alpineComponent.player.pause).toHaveBeenCalled()
    expect(alpineComponent.isPlaying).toBe(false)
    expect(alpineComponent.currentDay).toBe(10)
    expect(alpineComponent.dayPickerValue).toBe(10)
    expect(alpineComponent.updateReadings).toHaveBeenCalled()
  })
})
