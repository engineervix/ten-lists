import config from './config.js'

// 1. Book name mapping to their file format names
export const bookNameMap = {
  // Old Testament (Testament A)
  'Genesis': {
    bookCode: '01',
    testament: 'A',
    name: 'Genesis',
    formattedName: 'Genesis_____',
  },
  'Exodus': {
    bookCode: '02',
    testament: 'A',
    name: 'Exodus',
    formattedName: 'Exodus______',
  },
  'Leviticus': {
    bookCode: '03',
    testament: 'A',
    name: 'Leviticus',
    formattedName: 'Leviticus___',
  },
  'Numbers': {
    bookCode: '04',
    testament: 'A',
    name: 'Numbers',
    formattedName: 'Numbers_____',
  },
  'Deuteronomy': {
    bookCode: '05',
    testament: 'A',
    name: 'Deuteronomy',
    formattedName: 'Deuteronomy_',
  },
  'Joshua': {
    bookCode: '06',
    testament: 'A',
    name: 'Joshua',
    formattedName: 'Joshua______',
  },
  'Judges': {
    bookCode: '07',
    testament: 'A',
    name: 'Judges',
    formattedName: 'Judges______',
  },
  'Ruth': {
    bookCode: '08',
    testament: 'A',
    name: 'Ruth',
    formattedName: 'Ruth________',
  },
  '1 Samuel': {
    bookCode: '09',
    testament: 'A',
    name: '1 Samuel',
    formattedName: '1Samuel_____',
  },
  '2 Samuel': {
    bookCode: '10',
    testament: 'A',
    name: '2 Samuel',
    formattedName: '2Samuel_____',
  },
  '1 Kings': {
    bookCode: '11',
    testament: 'A',
    name: '1 Kings',
    formattedName: '1Kings______',
  },
  '2 Kings': {
    bookCode: '12',
    testament: 'A',
    name: '2 Kings',
    formattedName: '2Kings______',
  },
  '1 Chronicles': {
    bookCode: '13',
    testament: 'A',
    name: '1 Chronicles',
    formattedName: '1Chronicles_',
  },
  '2 Chronicles': {
    bookCode: '14',
    testament: 'A',
    name: '2 Chronicles',
    formattedName: '2Chronicles_',
  },
  'Ezra': {
    bookCode: '15',
    testament: 'A',
    name: 'Ezra',
    formattedName: 'Ezra________',
  },
  'Nehemiah': {
    bookCode: '16',
    testament: 'A',
    name: 'Nehemiah',
    formattedName: 'Nehemiah____',
  },
  'Esther': {
    bookCode: '17',
    testament: 'A',
    name: 'Esther',
    formattedName: 'Esther______',
  },
  'Job': {
    bookCode: '18',
    testament: 'A',
    name: 'Job',
    formattedName: 'Job_________',
  },
  'Psalms': {
    bookCode: '19',
    testament: 'A',
    name: 'Psalms',
    formattedName: 'Psalms______',
  },
  'Proverbs': {
    bookCode: '20',
    testament: 'A',
    name: 'Proverbs',
    formattedName: 'Proverbs____',
  },
  'Ecclesiastes': {
    bookCode: '21',
    testament: 'A',
    name: 'Ecclesiastes',
    formattedName: 'Ecclesiastes',
  },
  'Song of Solomon': {
    bookCode: '22',
    testament: 'A',
    name: 'Song of Solomon',
    formattedName: 'SongofSongs_',
  },
  'Isaiah': {
    bookCode: '23',
    testament: 'A',
    name: 'Isaiah',
    formattedName: 'Isaiah______',
  },
  'Jeremiah': {
    bookCode: '24',
    testament: 'A',
    name: 'Jeremiah',
    formattedName: 'Jeremiah____',
  },
  'Lamentations': {
    bookCode: '25',
    testament: 'A',
    name: 'Lamentations',
    formattedName: 'Lamentations',
  },
  'Ezekiel': {
    bookCode: '26',
    testament: 'A',
    name: 'Ezekiel',
    formattedName: 'Ezekiel_____',
  },
  'Daniel': {
    bookCode: '27',
    testament: 'A',
    name: 'Daniel',
    formattedName: 'Daniel______',
  },
  'Hosea': {
    bookCode: '28',
    testament: 'A',
    name: 'Hosea',
    formattedName: 'Hosea_______',
  },
  'Joel': {
    bookCode: '29',
    testament: 'A',
    name: 'Joel',
    formattedName: 'Joel________',
  },
  'Amos': {
    bookCode: '30',
    testament: 'A',
    name: 'Amos',
    formattedName: 'Amos________',
  },
  'Obadiah': {
    bookCode: '31',
    testament: 'A',
    name: 'Obadiah',
    formattedName: 'Obadiah_____',
  },
  'Jonah': {
    bookCode: '32',
    testament: 'A',
    name: 'Jonah',
    formattedName: 'Jonah_______',
  },
  'Micah': {
    bookCode: '33',
    testament: 'A',
    name: 'Micah',
    formattedName: 'Micah_______',
  },
  'Nahum': {
    bookCode: '34',
    testament: 'A',
    name: 'Nahum',
    formattedName: 'Nahum_______',
  },
  'Habakkuk': {
    bookCode: '35',
    testament: 'A',
    name: 'Habakkuk',
    formattedName: 'Habakkuk____',
  },
  'Zephaniah': {
    bookCode: '36',
    testament: 'A',
    name: 'Zephaniah',
    formattedName: 'Zephaniah___',
  },
  'Haggai': {
    bookCode: '37',
    testament: 'A',
    name: 'Haggai',
    formattedName: 'Haggai______',
  },
  'Zechariah': {
    bookCode: '38',
    testament: 'A',
    name: 'Zechariah',
    formattedName: 'Zechariah___',
  },
  'Malachi': {
    bookCode: '39',
    testament: 'A',
    name: 'Malachi',
    formattedName: 'Malachi_____',
  },

  // New Testament (Testament B)
  'Matthew': {
    bookCode: '01',
    testament: 'B',
    name: 'Matthew',
    formattedName: 'Matthew_____',
  },
  'Mark': {
    bookCode: '02',
    testament: 'B',
    name: 'Mark',
    formattedName: 'Mark________',
  },
  'Luke': {
    bookCode: '03',
    testament: 'B',
    name: 'Luke',
    formattedName: 'Luke________',
  },
  'John': {
    bookCode: '04',
    testament: 'B',
    name: 'John',
    formattedName: 'John________',
  },
  'Acts': {
    bookCode: '05',
    testament: 'B',
    name: 'Acts',
    formattedName: 'Acts________',
  },
  'Romans': {
    bookCode: '06',
    testament: 'B',
    name: 'Romans',
    formattedName: 'Romans______',
  },
  '1 Corinthians': {
    bookCode: '07',
    testament: 'B',
    name: '1 Corinthians',
    formattedName: '1Corinthians',
  },
  '2 Corinthians': {
    bookCode: '08',
    testament: 'B',
    name: '2 Corinthians',
    formattedName: '2Corinthians',
  },
  'Galatians': {
    bookCode: '09',
    testament: 'B',
    name: 'Galatians',
    formattedName: 'Galatians___',
  },
  'Ephesians': {
    bookCode: '10',
    testament: 'B',
    name: 'Ephesians',
    formattedName: 'Ephesians___',
  },
  'Philippians': {
    bookCode: '11',
    testament: 'B',
    name: 'Philippians',
    formattedName: 'Philippians_',
  },
  'Colossians': {
    bookCode: '12',
    testament: 'B',
    name: 'Colossians',
    formattedName: 'Colossians__',
  },
  '1 Thessalonians': {
    bookCode: '13',
    testament: 'B',
    name: '1 Thessalonians',
    formattedName: '1Thess______',
  },
  '2 Thessalonians': {
    bookCode: '14',
    testament: 'B',
    name: '2 Thessalonians',
    formattedName: '2Thess______',
  },
  '1 Timothy': {
    bookCode: '15',
    testament: 'B',
    name: '1 Timothy',
    formattedName: '1Timothy____',
  },
  '2 Timothy': {
    bookCode: '16',
    testament: 'B',
    name: '2 Timothy',
    formattedName: '2Timothy____',
  },
  'Titus': {
    bookCode: '17',
    testament: 'B',
    name: 'Titus',
    formattedName: 'Titus_______',
  },
  'Philemon': {
    bookCode: '18',
    testament: 'B',
    name: 'Philemon',
    formattedName: 'Philemon____',
  },
  'Hebrews': {
    bookCode: '19',
    testament: 'B',
    name: 'Hebrews',
    formattedName: 'Hebrews_____',
  },
  'James': {
    bookCode: '20',
    testament: 'B',
    name: 'James',
    formattedName: 'James_______',
  },
  '1 Peter': {
    bookCode: '21',
    testament: 'B',
    name: '1 Peter',
    formattedName: '1Peter______',
  },
  '2 Peter': {
    bookCode: '22',
    testament: 'B',
    name: '2 Peter',
    formattedName: '2Peter______',
  },
  '1 John': {
    bookCode: '23',
    testament: 'B',
    name: '1 John',
    formattedName: '1John_______',
  },
  '2 John': {
    bookCode: '24',
    testament: 'B',
    name: '2 John',
    formattedName: '2John_______',
  },
  '3 John': {
    bookCode: '25',
    testament: 'B',
    name: '3 John',
    formattedName: '3John_______',
  },
  'Jude': {
    bookCode: '26',
    testament: 'B',
    name: 'Jude',
    formattedName: 'Jude________',
  },
  'Revelation': {
    bookCode: '27',
    testament: 'B',
    name: 'Revelation',
    formattedName: 'Revelation__',
  },
}

// 2. Define the reading lists
export const tenLists = [
  {
    id: 1,
    name: 'Gospels',
    books: ['Matthew', 'Mark', 'Luke', 'John'],
    totalDays: 89,
  },
  {
    id: 2,
    name: 'Pentateuch',
    books: ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy'],
    totalDays: 187,
  },
  {
    id: 3,
    name: "Paul's Epistles & Hebrews",
    books: [
      'Romans',
      '1 Corinthians',
      '2 Corinthians',
      'Galatians',
      'Ephesians',
      'Philippians',
      'Colossians',
      'Hebrews',
    ],
    totalDays: 78,
  },
  {
    id: 4,
    name: 'Epistles & Revelation',
    books: [
      '1 Thessalonians',
      '2 Thessalonians',
      '1 Timothy',
      '2 Timothy',
      'Titus',
      'Philemon',
      'James',
      '1 Peter',
      '2 Peter',
      '1 John',
      '2 John',
      '3 John',
      'Jude',
      'Revelation',
    ],
    totalDays: 65,
  },
  {
    id: 5,
    name: 'Old Testament Wisdom Literature',
    books: ['Job', 'Ecclesiastes', 'Song of Solomon'],
    totalDays: 62,
  },
  {
    id: 6,
    name: 'Psalms',
    books: ['Psalms'],
    totalDays: 150,
  },
  {
    id: 7,
    name: 'Proverbs',
    books: ['Proverbs'],
    totalDays: 31,
  },
  {
    id: 8,
    name: 'Old Testament History',
    books: [
      'Joshua',
      'Judges',
      'Ruth',
      '1 Samuel',
      '2 Samuel',
      '1 Kings',
      '2 Kings',
      '1 Chronicles',
      '2 Chronicles',
      'Ezra',
      'Nehemiah',
      'Esther',
    ],
    totalDays: 249,
  },
  {
    id: 9,
    name: 'Old Testament Prophets',
    books: [
      'Isaiah',
      'Jeremiah',
      'Lamentations',
      'Ezekiel',
      'Daniel',
      'Hosea',
      'Joel',
      'Amos',
      'Obadiah',
      'Jonah',
      'Micah',
      'Nahum',
      'Habakkuk',
      'Zephaniah',
      'Haggai',
      'Zechariah',
      'Malachi',
    ],
    totalDays: 250,
  },
  {
    id: 10,
    name: 'Acts',
    books: ['Acts'],
    totalDays: 28,
  },
]

// 3. Function to get the number of chapters in a book
export function getChapterCount(bookName) {
  // This is a lookup table for the number of chapters in each book
  const chapterCounts = {
    'Genesis': 50,
    'Exodus': 40,
    'Leviticus': 27,
    'Numbers': 36,
    'Deuteronomy': 34,
    'Joshua': 24,
    'Judges': 21,
    'Ruth': 4,
    '1 Samuel': 31,
    '2 Samuel': 24,
    '1 Kings': 22,
    '2 Kings': 25,
    '1 Chronicles': 29,
    '2 Chronicles': 36,
    'Ezra': 10,
    'Nehemiah': 13,
    'Esther': 10,
    'Job': 42,
    'Psalms': 150,
    'Proverbs': 31,
    'Ecclesiastes': 12,
    'Song of Solomon': 8,
    'Isaiah': 66,
    'Jeremiah': 52,
    'Lamentations': 5,
    'Ezekiel': 48,
    'Daniel': 12,
    'Hosea': 14,
    'Joel': 3,
    'Amos': 9,
    'Obadiah': 1,
    'Jonah': 4,
    'Micah': 7,
    'Nahum': 3,
    'Habakkuk': 3,
    'Zephaniah': 3,
    'Haggai': 2,
    'Zechariah': 14,
    'Malachi': 4,
    'Matthew': 28,
    'Mark': 16,
    'Luke': 24,
    'John': 21,
    'Acts': 28,
    'Romans': 16,
    '1 Corinthians': 16,
    '2 Corinthians': 13,
    'Galatians': 6,
    'Ephesians': 6,
    'Philippians': 4,
    'Colossians': 4,
    '1 Thessalonians': 5,
    '2 Thessalonians': 3,
    '1 Timothy': 6,
    '2 Timothy': 4,
    'Titus': 3,
    'Philemon': 1,
    'Hebrews': 13,
    'James': 5,
    '1 Peter': 5,
    '2 Peter': 3,
    '1 John': 5,
    '2 John': 1,
    '3 John': 1,
    'Jude': 1,
    'Revelation': 22,
  }

  return chapterCounts[bookName] || 0
}

// 4. Function to generate the audio file path
export function getAudioFilePath(bookName, chapter) {
  const bookInfo = bookNameMap[bookName]
  if (!bookInfo) {
    console.error(`Book not found: ${bookName}`)
    return ''
  }

  // Format the chapter number with leading zero if needed
  const chapterFormatted = chapter.toString().padStart(2, '0')

  // Special handling for Psalms which uses a different format (3 digits for chapter)
  let fileName
  if (bookName === 'Psalms') {
    // Format Psalms chapters with three digits
    const psalmChapterFormatted = chapter.toString().padStart(3, '0')
    fileName = `${bookInfo.testament}${bookInfo.bookCode}__${psalmChapterFormatted}_${bookInfo.formattedName}ENGESVC2DA.mp3`
  } else {
    // Standard format for all other books
    fileName = `${bookInfo.testament}${bookInfo.bookCode}___${chapterFormatted}_${bookInfo.formattedName}ENGESVC2DA.mp3`
  }

  // Get the base URL from config - this automatically handles development vs. production
  const baseUrl = config.storage.getBaseUrl()

  return `${baseUrl}/${fileName}`
}

// Function to validate if a file path exists in the available files
// This is a fallback function to handle potential discrepancies
export function validateFilePath(filePath, availableFiles) {
  // In production, we would implement this to check against
  // an actual list of available files or make an API call

  // For now, let's just return true and handle errors during playback
  return true
}

// 5. Function to generate the reading plan for a specific day
export function generateReadingPlan(day) {
  if (!day || day < 1) {
    console.error('Invalid day provided. Using day 1 instead.')
    day = 1
  }

  const readings = []

  // For each of the 10 lists
  tenLists.forEach((list) => {
    // Calculate which chapter to read from this list
    // If day is greater than totalDays, we need to loop back to the beginning
    let chapterIndex = (day - 1) % list.totalDays

    // Initialize variables to track current book and chapter
    let currentBookIndex = 0
    let currentChapter = 1

    // Keep track of how many chapters we've gone through
    let chapterCount = 0

    // Loop through books in this list
    for (let i = 0; i < list.books.length; i++) {
      const bookName = list.books[i]
      // Get the number of chapters for this book
      const chaptersInBook = getChapterCount(bookName)

      // If adding the chapters in this book would exceed our target index,
      // this is the book we want
      if (chapterCount + chaptersInBook > chapterIndex) {
        currentBookIndex = i
        currentChapter = chapterIndex - chapterCount + 1
        break
      }

      // Otherwise, add the chapters in this book to our count and continue
      chapterCount += chaptersInBook
    }

    // Get the book name
    const book = list.books[currentBookIndex]

    // Get the file path for this reading
    const filePath = getAudioFilePath(book, currentChapter)

    // Add this reading to our list
    readings.push({
      listId: list.id,
      listName: list.name,
      book: book,
      chapter: currentChapter,
      filePath: filePath,
      reference: `${book} ${currentChapter}`,
    })
  })

  return readings
}

// Utility function to test file path generation for debugging
export function testFilePathGeneration() {
  const testCases = [
    { book: 'Genesis', chapter: 1 },
    { book: 'Psalms', chapter: 1 },
    { book: 'Psalms', chapter: 100 },
    { book: 'Matthew', chapter: 1 },
    { book: 'Revelation', chapter: 22 },
  ]

  console.log('Testing file path generation:')
  testCases.forEach(({ book, chapter }) => {
    const filePath = getAudioFilePath(book, chapter)
    console.log(`${book} ${chapter}: ${filePath}`)
  })
}

// 6. Function to generate ESV.org URL for all readings
export function generateESVUrl(readings) {
  if (!readings || readings.length === 0) {
    return ''
  }

  // ESV.org base URL for Bible reading
  const baseUrl = 'https://www.esv.org/verses/'

  // Map of book names that need special formatting for ESV.org
  const esvBookNameMap = {
    'Song of Solomon': 'Song+of+Solomon',
    '1 Samuel': '1+Samuel',
    '2 Samuel': '2+Samuel',
    '1 Kings': '1+Kings',
    '2 Kings': '2+Kings',
    '1 Chronicles': '1+Chronicles',
    '2 Chronicles': '2+Chronicles',
    '1 Corinthians': '1+Corinthians',
    '2 Corinthians': '2+Corinthians',
    '1 Thessalonians': '1+Thessalonians',
    '2 Thessalonians': '2+Thessalonians',
    '1 Timothy': '1+Timothy',
    '2 Timothy': '2+Timothy',
    '1 Peter': '1+Peter',
    '2 Peter': '2+Peter',
    '1 John': '1+John',
    '2 John': '2+John',
    '3 John': '3+John',
  }

  // Map each reading to the ESV format reference and join with semicolons
  const references = readings
    .map((reading) => {
      // Convert book name to ESV.org format if needed
      const bookName = esvBookNameMap[reading.book] || reading.book.replace(/\s+/g, '+')
      return `${bookName}+${reading.chapter}`
    })
    .join(';')

  // Construct the final URL
  return `${baseUrl}${references}/`
}
