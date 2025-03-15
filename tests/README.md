# Testing ten-lists

This directory contains all the tests for the ten-lists application.

## Overview

We use [Vitest](https://vitest.dev/) as our testing framework, which is designed to work seamlessly with Vite. The tests are organized as follows:

- `unit/`: Unit tests for individual modules and functions
- `integration/`: Tests that check how different parts work together
- `mocks/`: Mock implementations for browser APIs and external dependencies

## Running the Tests

To run the tests, use one of the following commands:

```bash
# Run tests in watch mode
npm test

# Run tests with coverage report
npm run test:cov
```

## Test Structure

Each test file follows the structure of:

1. Imports and mocks
2. Test suite definitions with `describe`
3. Individual test cases with `it` or `test`
4. Setup and teardown with `beforeEach` and `afterEach`

For example:

```javascript
import { describe, it, expect, beforeEach, vi } from 'vitest'
import { myFunction } from '../src/myModule.js'

// Mock dependencies
vi.mock('../src/dependency.js')

describe('My Function', () => {
  beforeEach(() => {
    // Setup
  })

  it('does something specific', () => {
    // Test
  })
})
```

## Mocks

We provide mock implementations for browser APIs in `mocks/browserMocks.js`. These include:

- `localStorage`
- `matchMedia`
- Audio APIs
- DOM elements
- External libraries like Plyr.io and BLB ScriptTagger

## Coverage

Run `npm run test:cov` to generate a coverage report. This will show how much of the codebase is covered by tests.

## Writing New Tests

When adding new features:

1. Create a new test file in the appropriate directory
2. Import the functionality you want to test
3. Mock any dependencies
4. Write test cases to verify behavior
5. Run the tests to ensure they pass

## Tips

- Use `vi.mock()` to mock modules
- Use `vi.spyOn()` to spy on functions and verify they're called
- Use `vi.fn()` for creating mock functions
- Prefer `beforeEach` for setup to ensure a clean state for each test
- Use `afterEach` for cleanup if needed
