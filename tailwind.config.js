/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            a: {
              'color': 'hsl(var(--p))',
              '&:hover': {
                color: 'hsl(var(--pf))',
              },
            },
          },
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography'), require('daisyui')],
  daisyui: {
    themes: ['winter', 'night'],
  },
  darkMode: ['selector', '[data-theme="night"]'],
}
