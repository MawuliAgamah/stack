

VITE_CONFIG = """
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 3000
  }
})
"""

TAILWIND_CONFIG_JS = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}"""


POST_CSS_CONFIG = """
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""

TEMPLATES = {
    'vite.config.js':VITE_CONFIG,
    'tailwind.config.js':TAILWIND_CONFIG_JS,
    'postcss.config.js':POST_CSS_CONFIG
}
