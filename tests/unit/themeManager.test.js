import { describe, it, expect, beforeEach, vi, afterEach } from 'vitest'
import { themeManager } from '../../src/js/themeManager.js'

describe('ThemeManager', () => {
  // Setup DOM and localStorage mocks before each test
  beforeEach(() => {
    // Create a mocked document element
    document.documentElement.setAttribute = vi.fn()
    document.documentElement.getAttribute = vi.fn()

    // Mock localStorage
    vi.spyOn(Storage.prototype, 'getItem')
    vi.spyOn(Storage.prototype, 'setItem')

    // Mock window.matchMedia
    window.matchMedia = vi.fn().mockImplementation((query) => {
      return {
        matches: false,
        media: query,
        // Support both old API (addListener) and new API (addEventListener)
        addEventListener: vi.fn(),
        removeEventListener: vi.fn(),
        addListener: vi.fn(),
        removeListener: vi.fn(),
      }
    })

    // Reset all mocks
    vi.resetAllMocks()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  describe('init', () => {
    it('loads theme from localStorage if available', () => {
      // Setup
      localStorage.getItem.mockReturnValue('night')

      // We need to mock the matchMedia result more comprehensively for this test
      const matchMediaMock = {
        matches: false,
        media: '(prefers-color-scheme: dark)',
        addEventListener: vi.fn(),
        removeEventListener: vi.fn(),
        addListener: vi.fn(), // For older browsers
        removeListener: vi.fn(), // For older browsers
      }
      window.matchMedia.mockReturnValue(matchMediaMock)

      // Execute
      themeManager.init()

      // Verify
      expect(localStorage.getItem).toHaveBeenCalledWith(themeManager.STORAGE_KEY)
      expect(document.documentElement.setAttribute).toHaveBeenCalledWith('data-theme', 'night')

      // It should attempt to add an event listener for theme changes
      expect(matchMediaMock.addEventListener).toHaveBeenCalledWith('change', expect.any(Function))
    })

    it('uses system preference if no saved theme', () => {
      // Setup
      localStorage.getItem.mockReturnValue(null)
      const matchMediaMock = {
        matches: true,
        media: '(prefers-color-scheme: dark)',
        addEventListener: vi.fn(),
        removeEventListener: vi.fn(),
        addListener: vi.fn(),
        removeListener: vi.fn(),
      }
      window.matchMedia.mockReturnValue(matchMediaMock)

      // Execute
      themeManager.init()

      // Verify
      expect(document.documentElement.setAttribute).toHaveBeenCalledWith(
        'data-theme',
        themeManager.THEMES.DARK
      )
    })

    it('sets up listener for system theme changes', () => {
      // Setup
      const matchMediaMock = {
        matches: false,
        media: '(prefers-color-scheme: dark)',
        addEventListener: vi.fn(),
        removeEventListener: vi.fn(),
        addListener: vi.fn(),
        removeListener: vi.fn(),
      }
      window.matchMedia.mockReturnValue(matchMediaMock)

      // Execute
      themeManager.init()

      // Verify
      expect(window.matchMedia).toHaveBeenCalledWith('(prefers-color-scheme: dark)')
      expect(matchMediaMock.addEventListener).toHaveBeenCalledWith('change', expect.any(Function))
    })
  })

  describe('toggleTheme', () => {
    it('toggles from light to dark theme', () => {
      // Setup
      document.documentElement.getAttribute.mockReturnValue(themeManager.THEMES.LIGHT)

      // Execute
      const result = themeManager.toggleTheme()

      // Verify
      expect(document.documentElement.setAttribute).toHaveBeenCalledWith(
        'data-theme',
        themeManager.THEMES.DARK
      )
      expect(localStorage.setItem).toHaveBeenCalledWith(
        themeManager.STORAGE_KEY,
        themeManager.THEMES.DARK
      )
      expect(result).toBe(themeManager.THEMES.DARK)
    })

    it('toggles from dark to light theme', () => {
      // Setup
      document.documentElement.getAttribute.mockReturnValue(themeManager.THEMES.DARK)

      // Execute
      const result = themeManager.toggleTheme()

      // Verify
      expect(document.documentElement.setAttribute).toHaveBeenCalledWith(
        'data-theme',
        themeManager.THEMES.LIGHT
      )
      expect(localStorage.setItem).toHaveBeenCalledWith(
        themeManager.STORAGE_KEY,
        themeManager.THEMES.LIGHT
      )
      expect(result).toBe(themeManager.THEMES.LIGHT)
    })
  })

  describe('setTheme', () => {
    it('sets the specified theme', () => {
      // Execute
      const result = themeManager.setTheme('custom-theme')

      // Verify
      expect(document.documentElement.setAttribute).toHaveBeenCalledWith(
        'data-theme',
        'custom-theme'
      )
      expect(localStorage.setItem).toHaveBeenCalledWith(themeManager.STORAGE_KEY, 'custom-theme')
      expect(result).toBe('custom-theme')
    })
  })

  describe('getCurrentTheme', () => {
    it('returns the current theme', () => {
      // Setup
      document.documentElement.getAttribute.mockReturnValue('test-theme')

      // Execute & Verify
      expect(themeManager.getCurrentTheme()).toBe('test-theme')
    })

    it('returns the default light theme if no theme set', () => {
      // Setup
      document.documentElement.getAttribute.mockReturnValue(null)

      // Execute & Verify
      expect(themeManager.getCurrentTheme()).toBe(themeManager.THEMES.LIGHT)
    })
  })

  describe('isDarkTheme', () => {
    it('returns true when current theme is dark', () => {
      // Setup
      vi.spyOn(themeManager, 'getCurrentTheme').mockReturnValue(themeManager.THEMES.DARK)

      // Execute & Verify
      expect(themeManager.isDarkTheme()).toBe(true)
    })

    it('returns false when current theme is not dark', () => {
      // Setup
      vi.spyOn(themeManager, 'getCurrentTheme').mockReturnValue(themeManager.THEMES.LIGHT)

      // Execute & Verify
      expect(themeManager.isDarkTheme()).toBe(false)
    })
  })
})
