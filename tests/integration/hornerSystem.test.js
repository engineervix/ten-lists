import { describe, it, expect, beforeEach, vi } from 'vitest'
import { generateReadingPlan, tenLists } from '../../src/js/main.js'

// Mock the config module
vi.mock('../../src/js/config.js', () => {
  return {
    default: {
      storage: {
        getBaseUrl: () => '/audio',
      },
    },
  }
})

describe('Ten Lists Bible Reading System', () => {
  describe('System Structure', () => {
    it('has exactly 10 reading lists', () => {
      expect(tenLists).toHaveLength(10)
    })

    it('each list has the required properties', () => {
      tenLists.forEach((list) => {
        expect(list).toHaveProperty('id')
        expect(list).toHaveProperty('name')
        expect(list).toHaveProperty('books')
        expect(list).toHaveProperty('totalDays')
        expect(Array.isArray(list.books)).toBe(true)
        expect(typeof list.totalDays).toBe('number')
      })
    })
  })

  describe('Reading Plan Generation', () => {
    const validateReadingPlan = (readings) => {
      // Each reading plan should have 10 readings, one from each list
      expect(readings).toHaveLength(10)

      // Each reading should be from a different list
      const listIds = readings.map((r) => r.listId)
      expect(new Set(listIds).size).toBe(10)

      // Each reading should have the required properties
      readings.forEach((reading) => {
        expect(reading).toHaveProperty('listId')
        expect(reading).toHaveProperty('listName')
        expect(reading).toHaveProperty('book')
        expect(reading).toHaveProperty('chapter')
        expect(reading).toHaveProperty('filePath')
        expect(reading).toHaveProperty('reference')

        // Validate the reference format
        expect(reading.reference).toBe(`${reading.book} ${reading.chapter}`)

        // Validate file path format
        if (reading.book === 'Psalms') {
          // Special format for Psalms
          expect(reading.filePath).toMatch(/^\/audio\/A19__\d{3}_Psalms______ENGESVC2DA\.mp3$/)
        } else {
          // Standard format for all other books
          expect(reading.filePath).toMatch(/^\/audio\/[AB]\d{2}___\d{2}_.*ENGESVC2DA\.mp3$/)
        }
      })
    }

    it('generates valid reading plan for day 1', () => {
      const readings = generateReadingPlan(1)
      validateReadingPlan(readings)

      // Day 1 should have the first chapter of the first book in each list
      expect(readings[0].book).toBe('Matthew')
      expect(readings[0].chapter).toBe(1)

      expect(readings[1].book).toBe('Genesis')
      expect(readings[1].chapter).toBe(1)

      expect(readings[5].book).toBe('Psalms')
      expect(readings[5].chapter).toBe(1)

      expect(readings[9].book).toBe('Acts')
      expect(readings[9].chapter).toBe(1)
    })

    it('generates valid reading plan for day 30', () => {
      const readings = generateReadingPlan(30)
      validateReadingPlan(readings)

      // For list 7 (Proverbs, which has 31 days), we should be on chapter 30
      const proverbsReading = readings.find((r) => r.listId === 7)
      expect(proverbsReading.book).toBe('Proverbs')
      expect(proverbsReading.chapter).toBe(30)

      // For list 10 (Acts, which has 28 days), we should be on chapter 2 of the second cycle
      const actsReading = readings.find((r) => r.listId === 10)
      expect(actsReading.book).toBe('Acts')
      expect(actsReading.chapter).toBe(2)
    })

    it('generates valid reading plan for day 100', () => {
      const readings = generateReadingPlan(100)
      validateReadingPlan(readings)
    })

    it('generates valid reading plan for day 365', () => {
      const readings = generateReadingPlan(365)
      validateReadingPlan(readings)
    })

    it('generates valid reading plan for very large day number', () => {
      // Testing with a very large day number to ensure the modulo arithmetic works correctly
      const readings = generateReadingPlan(1000)
      validateReadingPlan(readings)
    })

    it('each list cycles correctly based on its totalDays', () => {
      // Test that lists cycle back to the beginning correctly
      tenLists.forEach((list) => {
        // Get readings for day 1 and day (1 + totalDays)
        const day1Readings = generateReadingPlan(1)
        const dayCycleReadings = generateReadingPlan(1 + list.totalDays)

        // Find the readings for this list ID in both sets
        const day1Reading = day1Readings.find((r) => r.listId === list.id)
        const dayCycleReading = dayCycleReadings.find((r) => r.listId === list.id)

        // After one full cycle, we should be back to the first chapter of the first book in this list
        expect(dayCycleReading.book).toBe(day1Reading.book)
        expect(dayCycleReading.chapter).toBe(day1Reading.chapter)
      })
    })
  })
})
