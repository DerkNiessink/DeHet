/**
 * App configuration file
 */

const config = {
  api: {
    baseUrl: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
    timeout: 30000, // 30 seconds
  },
  upload: {
    maxFileSize: 10 * 1024 * 1024, // 10MB
    acceptedFileTypes: ['.ics'],
  },
  app: {
    name: 'WhenItWorks',
    version: '1.0.0',
  }
};

export default config;