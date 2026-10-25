import react, { reactCompilerPreset } from '@vitejs/plugin-react'
import babel from '@rolldown/plugin-babel'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    babel({ presets: [reactCompilerPreset()] })
  ],
  server: {
    // Requests to /api/* are forwarded to the Django dev server.
    // Keeps the browser same-origin, so no CORS/CSRF headaches.
    proxy: {
      '/api': 'http://127.0.0.1:8000',
      '/admin': 'http://127.0.0.1:8000',
      '/static': 'http://127.0.0.1:8000',
    },
  },
})
