/**
 * Contains nuxt configuration
 */

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  ssr: false,
  css: ['~/assets/css/main.css'],

  runtimeConfig: {
    public: {
      apiBase: ''
    }
  },

  modules: [
    '@nuxt/eslint',
    '@nuxt/ui',
    '@nuxt/image',
    '@pinia/nuxt',
    'nuxt-lottie'
  ],

  lottie: {
    componentName: 'Lottie', // Optional: Customize the component name
    lottieFolder: '/assets/lottie', // Optional: Customize the Lottie folder path
    autoFolderCreation: true, // Optional: Auto create lottie folder (default: true)
    enableLogs: true // Optional: Enable console logs from module (default: true)
  },

  vite: {
    server: {
      allowedHosts: ['frontend']
    }
  },

  ui: {
    theme: {
      colors: [
        'primary',
        'secondary',
        'tertiary',
        'info',
        'success',
        'warning',
        'error',
        'accent'
      ]
    }
  },

  colorMode: {
    preference: 'dark'
  },

  app: {
    layoutTransition: { name: 'layout', mode: 'out-in' },
    pageTransition: { name: 'page', mode: 'out-in' }
  },

  // Font configuration
  fonts: {
    defaults: {
      weights: [300, 400, 500, 600, 700, 800, 900],
      styles: ['normal', 'italic']
    },
    families: [
      {
        name: 'Inter',
        provider: 'google',
        weights: [300, 400, 500, 600, 700, 800],
        styles: ['normal', 'italic'],
        display: 'swap'
      },
      {
        name: 'Poppins',
        provider: 'google',
        weights: [300, 400, 500, 600, 700, 800],
        styles: ['normal', 'italic'],
        display: 'swap'
      }
    ]
  }
});
