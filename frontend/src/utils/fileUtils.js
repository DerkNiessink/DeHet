/**
 * Contains helper functions for file handling operations
 */

/**
 * Reads a file and returns its contents as text
 * @param {File} file - The file to read
 * @returns {Promise<string>} - The file contents as text
 */
export const readFileAsText = (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();

        reader.onload = (event) => {
            resolve(event.target.result);
        };

        reader.onerror = (error) => {
            reject(error);
        };

        reader.readAsText(file);
    });
};

/**
 * Validates file type based on accepted extensions
 * @param {File} file - The file to validate
 * @param {Array<string>} acceptedTypes - Array of accepted file extensions
 * @returns {boolean} - Whether the file type is valid
 */
export const validateFileType = (file, acceptedTypes) => {
    if (!file || !acceptedTypes || !acceptedTypes.length) {
        return true; // No validation if no file or accepted types
    }

    const fileName = file.name || '';
    const fileExtension = fileName.split('.').pop().toLowerCase();

    return acceptedTypes.includes(fileExtension);
};

/**
 * Formats file size in a human-readable format
 * @param {number} bytes - File size in bytes
 * @returns {string} - Formatted file size
 */
export const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';

    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));

    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

export default {
    readFileAsText,
    validateFileType,
    formatFileSize
};