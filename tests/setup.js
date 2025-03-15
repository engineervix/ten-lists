// test setup file
import { vi } from 'vitest'

// Define globals that would be available in the browser
global.BLB = {
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

// Define __BUILD_DATE__ which is normally provided by Vite
global.__BUILD_DATE__ = JSON.stringify(new Date().toISOString())

// Mock fetch if not available
if (!global.fetch) {
  global.fetch = vi.fn()
}

// Set up local storage mock
if (!global.localStorage) {
  global.localStorage = {
    getItem: vi.fn(),
    setItem: vi.fn(),
    removeItem: vi.fn(),
    clear: vi.fn(),
  }
}

// Mock IntersectionObserver which isn't available in JSDOM
if (!global.IntersectionObserver) {
  global.IntersectionObserver = class IntersectionObserver {
    constructor() {
      this.observe = vi.fn()
      this.unobserve = vi.fn()
      this.disconnect = vi.fn()
    }
  }
}

// Mock MutationObserver which might not be fully implemented in JSDOM
if (!global.MutationObserver) {
  global.MutationObserver = class MutationObserver {
    constructor(callback) {
      this.callback = callback
      this.observe = vi.fn()
      this.disconnect = vi.fn()
      this.takeRecords = vi.fn()
    }
  }
}
