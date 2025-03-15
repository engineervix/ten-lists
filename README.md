# ten-lists

A web application that facilitates listening 👂🎧🔊 to the Holy Bible based on [Professor Grant Horner's Bible-Reading System](https://sohmer.net/media/professor_grant_horners_bible_reading_system.pdf).

<details>
  <summary>📱 Screenshot - Mobile</summary>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4f05409a-5ff3-4a70-ab72-4eda9df57d20" alt="mobile">
</p>
</details>

<details>
  <summary>🖥️ Screenshot - Desktop</summary>

![desktop](https://github.com/user-attachments/assets/85d38838-2b04-4dcc-afed-95320cc2b5f1)
</details>

[![Continuous Integration](https://github.com/engineervix/ten-lists/actions/workflows/main.yml/badge.svg)](https://github.com/engineervix/ten-lists/actions/workflows/main.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/engineervix/b8c0c76feb9db65c08ca3190cc90e46a/raw/covbadge.json)](https://github.com/engineervix/ten-lists/actions)

[![Node v22](https://img.shields.io/badge/Node-v22-teal.svg)](https://nodejs.org/en/blog/release/v22.0.0)
[![code style: prettier](https://img.shields.io/badge/code%20style-prettier-ff69b4.svg)](https://prettier.io/)

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Conventional Changelog](https://img.shields.io/badge/changelog-conventional-brightgreen.svg)](https://github.com/conventional-changelog)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Deployment](#deployment)
  - [Setting Up Your Cloud Storage](#setting-up-your-cloud-storage)
    - [Common Cloud Storage Options](#common-cloud-storage-options)
      - [Cloudflare R2](#cloudflare-r2)
      - [Backblaze B2](#backblaze-b2)
      - [AWS S3](#aws-s3)
  - [Cloudflare Pages](#cloudflare-pages)
  - [Other Platforms](#other-platforms)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Features

- Generate a playlist of 10 Bible chapters for any day in the bible reading plan.
- Audio playback of Bible chapters using [Plyr.io](https://plyr.io/)
- Responsive design with [tailwindcss](https://tailwindcss.com/)
- Interactive UI with [Alpine.js](https://alpinejs.dev/)
- Bible reference tooltips via [Blue Letter Bible ScriptTagger](https://www.blueletterbible.org/webtools/BLB_ScriptTagger.cfm)
- [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) to remember your current reading day

## Getting Started

### Prerequisites

- Node.js (v22 or higher)
- npm

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/engineervix/ten-lists.git
   cd ten-lists
   ```

2. Install dependencies:

   ```
   npm install
   ```

3. Set up audio files:

   - During development, audio files should be placed in a `/public/audio` directory
   - The audio files should follow this naming convention:
     - Old Testament: `A[book-code]___[chapter]_[formatted-name]ENGESVC2DA.mp3`
     - New Testament: `B[book-code]___[chapter]_[formatted-name]ENGESVC2DA.mp3`

   For example:

   - Job 1: `A18___01_Job_________ENGESVC2DA.mp3`
   - Song of Solomon 8: `A22___08_SongofSongs_ENGESVC2DA.mp3`
   - Acts 1: `B05___01_Acts________ENGESVC2DA.mp3`

   That's the convention used for the ESV dramatized audio Bible downloaded from the [_Faith Comes by Hearing®_ website](http://www.bible.is/audiodownloader).

4. Start the development server:

   ```
   npm run dev
   ```

5. Build for production:
   ```
   npm run build
   ```

## Deployment

You'll need the audio files to be hosted on cloud storage, e.g.

- Cloudflare R2
- Backblaze B2
- AWS S3

### Setting Up Your Cloud Storage

1. Create a bucket/container in your preferred cloud storage service.
2. Configure public access for the bucket (if you want files to be directly accessible).
3. Upload all audio files to the bucket.
4. Note your bucket URL.
5. Set up appropriate CORS settings.

#### Common Cloud Storage Options

##### Cloudflare R2

Your URL will typically be: `https://{account-id}.r2.cloudflarestorage.com/{bucket-name}`

##### Backblaze B2

Your URL will typically be: `https://{bucket-name}.s3.{region}.backblazeb2.com`

##### AWS S3

Your URL will typically be: `https://{bucket-name}.s3.amazonaws.com`

### Cloudflare Pages

This application can be deployed to Cloudflare Pages:

1. Connect your GitHub repository to Cloudflare Pages.
2. Configure the `VITE_MP3_BASE_URL` environment variable in the Cloudflare Pages dashboard.
3. Set the build command to `npm run build` and the build directory to `dist`.

### Other Platforms

You should be able to deploy to Github Pages, Gitlab Pages, Vercel, Netlify, and many other platforms. Check the respective platform docs.
