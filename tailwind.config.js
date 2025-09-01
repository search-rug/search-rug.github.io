/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ 
    '_includes/**/*.html',
    '_layouts/**/*.html',
    '_pages/**/*.html',
    '_pages/**/*.md'
  ],
  theme: {
    fontFamily: {
      sans: ['Work Sans', 'sans-serif'],
      serif: ['Brawler', 'serif'],
    },
    extend: {
      colors: {
        primary: '#e5261f',
        darkprimary: '#bb1c16',
        steel: '#5c5a5a',
        offwhite: '#fff6f8',
      },
      typography: {
        quoteless: {
          css: {
            'blockquote p:first-of-type::before': { content: 'none' },
            'blockquote p:first-of-type::after': { content: 'none' },
          },
        },
      },
    },
  },
  plugins: [
  ],
};
