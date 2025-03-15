/**
 * Browser environment mocks for testing
 * This file provides mock implementations of browser APIs that are used in the app
 */

// Local Storage Mock
export function setupLocalStorageMock() {
  const localStorageMock = (() => {
    let store = {}
    return {
      getItem: vi.fn((key) => store[key] || null),
      setItem: vi.fn((key, value) => {
        store[key] = value.toString()
      }),
      removeItem: vi.fn((key) => {
        delete store[key]
      }),
      clear: vi.fn(() => {
        store = {}
      }),
      length: 0,
      key: vi.fn(() => null),
    }
  })()

  Object.defineProperty(window, 'localStorage', {
    value: localStorageMock,
    writable: true,
  })

  return localStorageMock
}

// Match Media Mock
export function setupMatchMediaMock(mediaQueryMatch = false) {
  window.matchMedia = vi.fn().mockImplementation((query) => {
    return {
      matches: mediaQueryMatch,
      media: query,
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
      addListener: vi.fn(), // Deprecated but sometimes used
      removeListener: vi.fn(), // Deprecated but sometimes used
      dispatchEvent: vi.fn(),
    }
  })

  return window.matchMedia
}

// Audio Element Mock
export function setupAudioElementMock() {
  const AudioMock = vi.fn().mockImplementation(() => {
    return {
      play: vi.fn().mockResolvedValue(undefined),
      pause: vi.fn(),
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
      dispatchEvent: vi.fn(),
      src: '',
      currentTime: 0,
      volume: 1,
      muted: false,
    }
  })

  window.Audio = AudioMock
  return AudioMock
}

// PlyrJS Mock
export function setupPlyrMock() {
  const PlyrMock = vi.fn().mockImplementation(() => {
    return {
      source: null,
      playing: false,
      currentTime: 0,
      volume: 1,
      muted: false,
      play: vi.fn().mockResolvedValue(undefined),
      pause: vi.fn(),
      on: vi.fn(),
      off: vi.fn(),
      destroy: vi.fn(),
    }
  })

  return PlyrMock
}

// Window.BLB ScriptTagger Mock
export function setupBLBScriptTaggerMock() {
  window.BLB = {
    Tagger: {
      Translation: 'ESV',
      HyperLinks: 'all',
      HideTags: false,
      TargetNewWindow: true,
      Style: 'par',
      NoSearchTagNames: '',
      NoSearchClassNames: 'noTag doNotTag',
      tag: vi.fn(),
    },
  }

  return window.BLB
}

// Document Element Mock with data-theme support
export function setupDocumentElementMock() {
  const attributes = { 'data-theme': 'winter' }

  Object.defineProperty(document, 'documentElement', {
    value: {
      setAttribute: vi.fn((name, value) => {
        attributes[name] = value
      }),
      getAttribute: vi.fn((name) => attributes[name]),
      classList: {
        add: vi.fn(),
        remove: vi.fn(),
        contains: vi.fn(),
        toggle: vi.fn(),
      },
    },
    writable: true,
  })

  return document.documentElement
}

// Setup all mocks at once
export function setupAllBrowserMocks(options = {}) {
  const localStorage = setupLocalStorageMock()
  const matchMedia = setupMatchMediaMock(options.prefersDarkMode || false)
  const audio = setupAudioElementMock()
  const plyr = setupPlyrMock()
  const blb = setupBLBScriptTaggerMock()
  const documentElement = setupDocumentElementMock()

  return {
    localStorage,
    matchMedia,
    audio,
    plyr,
    blb,
    documentElement,
  }
}
