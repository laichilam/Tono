/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'core/templates/core/*.html',
    'userprofile/templates/userprofile/*.html',
    'item/templates/item/*.html',
    'room/templates/room/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'alu-red': '#D2691E',
        'alu-main': '#FEFBE9',
        'alu-netural': '#E1EEDD',
        'alu-three': '#F0A04B',
        'alu-btn': '#183A1D',
      },
    },
  },
  plugins: [

  ],
};
