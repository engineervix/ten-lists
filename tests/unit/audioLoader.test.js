import { describe, it, expect, beforeEach, vi, afterEach } from 'vitest'
import { AudioLoader } from '../../src/js/audioLoader.js'

// Mock the config module
vi.mock('../../src/js/config.js', () => {
  return {
    default: {
      isDevelopment: true,
    },
  }
})

describe('AudioLoader', () => {
  let audioLoader
  let mockPlayer

  // Setup before each test
  beforeEach(() => {
    // Reset fetch mocks
    global.fetch = vi.fn()

    // Create a new instance for each test
    audioLoader = new AudioLoader()

    // Mock player object
    mockPlayer = {
      source: null,
    }

    // Reset mocks
    vi.resetAllMocks()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  describe('checkFileAvailability', () => {
    it('returns true when file exists', async () => {
      // Mock a successful fetch response
      global.fetch.mockResolvedValueOnce({
        ok: true,
      })

      const result = await audioLoader.checkFileAvailability('test.mp3')
      expect(result).toBe(true)
      expect(global.fetch).toHaveBeenCalledWith('test.mp3', { method: 'HEAD' })
    })

    it('returns false when file does not exist', async () => {
      // Mock a failed fetch response
      global.fetch.mockResolvedValueOnce({
        ok: false,
      })

      const result = await audioLoader.checkFileAvailability('nonexistent.mp3')
      expect(result).toBe(false)
    })

    it('handles fetch errors', async () => {
      // Mock a fetch error
      global.fetch.mockRejectedValueOnce(new Error('Network error'))

      const result = await audioLoader.checkFileAvailability('error.mp3')
      expect(result).toBe(false)
    })

    it('caches results for subsequent calls', async () => {
      // Mock a successful fetch response
      global.fetch.mockResolvedValueOnce({
        ok: true,
      })

      // First call
      await audioLoader.checkFileAvailability('cached.mp3')

      // Second call to the same URL should use cached result
      await audioLoader.checkFileAvailability('cached.mp3')

      // Fetch should only be called once
      expect(global.fetch).toHaveBeenCalledTimes(1)
    })
  })

  describe('getErrorMessage', () => {
    it('returns development error message in dev mode', () => {
      const message = audioLoader.getErrorMessage('test.mp3')
      expect(message).toContain('local development')
      expect(message).toContain('test.mp3')
    })
  })

  describe('loadAudioWithRetry', () => {
    it('successfully loads audio when file is available', async () => {
      // Mock checkFileAvailability to return true
      vi.spyOn(audioLoader, 'checkFileAvailability').mockResolvedValue(true)

      const result = await audioLoader.loadAudioWithRetry('available.mp3', mockPlayer)

      expect(result).toBe(true)
      expect(mockPlayer.source).toEqual({
        type: 'audio',
        sources: [
          {
            src: 'available.mp3',
            type: 'audio/mp3',
          },
        ],
      })
    })

    it('retries when file check fails initially', async () => {
      // Mock checkFileAvailability to fail first, then succeed
      vi.spyOn(audioLoader, 'checkFileAvailability')
        .mockResolvedValueOnce(false)
        .mockResolvedValueOnce(true)

      const result = await audioLoader.loadAudioWithRetry('retry.mp3', mockPlayer)

      expect(result).toBe(true)
      expect(audioLoader.checkFileAvailability).toHaveBeenCalledTimes(2)
    })

    it('returns false after maximum retries', async () => {
      // Mock checkFileAvailability to always fail
      vi.spyOn(audioLoader, 'checkFileAvailability').mockResolvedValue(false)

      // Mock setTimeout to avoid waiting in tests
      vi.spyOn(global, 'setTimeout').mockImplementation((cb) => cb())

      const result = await audioLoader.loadAudioWithRetry('failing.mp3', mockPlayer)

      expect(result).toBe(false)
      // Should have tried 3 times (initial + 2 retries)
      expect(audioLoader.checkFileAvailability).toHaveBeenCalledTimes(3)
    })
  })
})
