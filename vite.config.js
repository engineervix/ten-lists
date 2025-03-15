import path from 'node:path'
import process from 'node:process'

import { defineConfig } from 'vite'

/**
 * Creates a sanitized base path from a repository or project name.
 * Used for configuring Vite's base URL in different deployment environments.
 *
 * @param {string} name - Repository or project name to convert into a path
 * @returns {string} Sanitized path starting and ending with '/', or just '/' if invalid input
 * @example
 * createBasePath('my-repo') // returns '/my-repo/'
 * createBasePath('my/repo') // returns '/myrepo/'
 * createBasePath('') // returns '/'
 */
const createBasePath = (name) => {
  if (!name) return '/'
  // Remove any special characters that might cause issues in URLs
  const sanitizedName = name.replace(/[^\w-]/g, '')
  return sanitizedName ? `/${sanitizedName}/` : '/'
}

/**
 * Determines the appropriate base path for Vite based on the deployment environment.
 * Supports GitHub Actions and GitLab CI deployments, with a fallback for local development.
 *
 * Environment variables used:
 * - GITHUB_ACTIONS: Present when running in GitHub Actions
 * - GITHUB_REPOSITORY: Format "username/repo-name"
 * - CI_PROJECT_PATH: GitLab CI project path
 *
 * References:
 * https://vite.dev/guide/static-deploy.html#github-pages
 * https://vite.dev/guide/static-deploy.html#gitlab-pages-and-gitlab-ci
 * https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables#default-environment-variables
 * https://docs.gitlab.com/ee/ci/variables/predefined_variables.html
 *
 * @returns {string} Base path for Vite configuration
 * @example
 * In GitHub Actions with GITHUB_REPOSITORY="user/my-repo"
 * getBasePathFromEnv() // returns '/my-repo/'
 *
 * In GitLab CI with CI_PROJECT_PATH="group/my-project"
 * getBasePathFromEnv() // returns '/my-project/'
 *
 * In local development
 * getBasePathFromEnv() // returns '/'
 */
const getBasePathFromEnv = () => {
  if (process.env.GITHUB_ACTIONS && process.env.GITHUB_REPOSITORY) {
    const [, repoName] = process.env.GITHUB_REPOSITORY.split('/')
    return createBasePath(repoName)
  }

  if (process.env.CI_PROJECT_PATH) {
    const projectName = process.env.CI_PROJECT_PATH.split('/').pop()
    return createBasePath(projectName)
  }

  return './'
}

export default defineConfig({
  // Base path for production build
  base: getBasePathFromEnv(),

  server: {
    open: process.env.NODE_ENV === 'development' ? true : false,
  },
  root: 'src',
  publicDir: '../public',
  build: {
    outDir: '../dist',
    emptyOutDir: true,
    sourcemap: true,
  },
  resolve: {
    alias: { '/src': path.resolve(process.cwd(), 'src') },
  },
  test: {
    include: ['../tests/**/*.test.js'],
    coverage: {
      all: true,
      provider: 'v8',
      reportsDirectory: '../.coverage',
      reporter: ['text', 'json', 'html', 'json-summary'],
    },
    environment: 'jsdom',
    globals: true,
    watch: false,
  },
  // Define global constants for the app
  define: {
    __BUILD_DATE__: JSON.stringify(new Date().toISOString()),
  },
})
