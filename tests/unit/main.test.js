import { describe, it, expect, beforeEach, vi } from 'vitest'
import {
  generateReadingPlan,
  getAudioFilePath,
  getChapterCount,
  bookNameMap,
  tenLists,
} from '../../src/js/main.js'

// Mock the config module
vi.mock('../../src/js/config.js', () => {
  return {
    default: {
      storage: {
        getBaseUrl: () => '/audio',
      },
      isDevelopment: true,
    },
  }
})

describe('Bible Reading Plan Functions', () => {
  describe('getChapterCount', () => {
    it('returns correct chapter count for Old Testament books', () => {
      expect(getChapterCount('Genesis')).toBe(50)
      expect(getChapterCount('Psalms')).toBe(150)
      expect(getChapterCount('Malachi')).toBe(4)
    })

    it('returns correct chapter count for New Testament books', () => {
      expect(getChapterCount('Matthew')).toBe(28)
      expect(getChapterCount('Acts')).toBe(28)
      expect(getChapterCount('Revelation')).toBe(22)
    })

    it('returns 0 for non-existent books', () => {
      expect(getChapterCount('NonExistentBook')).toBe(0)
    })
  })

  describe('getAudioFilePath', () => {
    it('generates correct file path for Genesis', () => {
      const path = getAudioFilePath('Genesis', 1)
      expect(path).toBe('/audio/A01___01_Genesis_____ENGESVC2DA.mp3')
    })

    it('generates correct file path for Psalms (special format)', () => {
      const path = getAudioFilePath('Psalms', 119)
      expect(path).toBe('/audio/A19__119_Psalms______ENGESVC2DA.mp3')
    })

    it('generates correct file path for New Testament', () => {
      const path = getAudioFilePath('John', 3)
      expect(path).toBe('/audio/B04___03_John________ENGESVC2DA.mp3')
    })

    it('pads chapter numbers with leading zeros', () => {
      const path = getAudioFilePath('Matthew', 1)
      expect(path).toContain('_01_')

      const path2 = getAudioFilePath('Matthew', 10)
      expect(path2).toContain('_10_')
    })

    it('returns empty string for invalid book', () => {
      const path = getAudioFilePath('InvalidBook', 1)
      expect(path).toBe('')
    })
  })

  describe('generateReadingPlan', () => {
    it('returns 10 readings for day 1', () => {
      const readings = generateReadingPlan(1)
      expect(readings).toHaveLength(10)

      // Check first day readings (should be chapter 1 of first book in each list)
      expect(readings[0].book).toBe('Matthew')
      expect(readings[0].chapter).toBe(1)
      expect(readings[1].book).toBe('Genesis')
      expect(readings[1].chapter).toBe(1)
    })

    it('handles invalid day input by defaulting to day 1', () => {
      const readings = generateReadingPlan(0)
      expect(readings).toHaveLength(10)
      expect(readings[0].book).toBe('Matthew')
      expect(readings[0].chapter).toBe(1)
    })

    it('loops back to the beginning of a list when reaching the end', () => {
      // Test with a day number that's higher than list 10's total (Acts has 28 chapters)
      const readings = generateReadingPlan(30)
      // For list 10 (Acts), we should be on chapter 2 of the second loop
      expect(readings[9].book).toBe('Acts')
      expect(readings[9].chapter).toBe(2)
    })

    it('generates correct references for readings', () => {
      const readings = generateReadingPlan(10)
      readings.forEach((reading) => {
        expect(reading.reference).toBe(`${reading.book} ${reading.chapter}`)
      })
    })

    it('generates file paths for all readings', () => {
      const readings = generateReadingPlan(1)
      readings.forEach((reading) => {
        expect(reading.filePath).toContain('/audio/')
        expect(reading.filePath).toContain('.mp3')
      })
    })
  })
})
