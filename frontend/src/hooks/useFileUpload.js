import { useState } from 'react';
import { readFileAsText, validateFileType, formatFileSize } from '../utils/fileUtils';
import config from '../configs/app.config';

/**
 * Custom hook for handling file uploads
 * @param {Object} options - Hook options
 * @param {Array<string>} options.acceptedTypes - Accepted file types
 * @param {number} options.maxSize - Maximum file size in bytes
 * @param {Function} options.onSuccess - Callback on successful upload
 * @param {Function} options.onError - Callback on upload error
 * @returns {Object} - Hook state and methods
 */
const useFileUpload = (options = {}) => {
    const {
        acceptedTypes = config.upload.acceptedFileTypes,
        maxSize = config.upload.maxFileSize,
        onSuccess = () => { },
        onError = () => { },
    } = options;

    const [file, setFile] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleFileChange = async (event) => {
        const selectedFile = event.target.files[0];
        setError(null);

        if (!selectedFile) {
            return;
        }

        // Validate file type
        if (acceptedTypes.length > 0 && !validateFileType(selectedFile, acceptedTypes)) {
            const errorMessage = `Invalid file type. Accepted types: ${acceptedTypes.join(', ')}`;
            setError(errorMessage);
            onError(errorMessage);
            return;
        }

        // Validate file size
        if (selectedFile.size > maxSize) {
            const errorMessage = `File is too large. Maximum size: ${formatFileSize(maxSize)}`;
            setError(errorMessage);
            onError(errorMessage);
            return;
        }

        setFile(selectedFile);

        try {
            setIsLoading(true);
            const content = await readFileAsText(selectedFile);
            onSuccess(content, selectedFile);
        } catch (err) {
            const errorMessage = 'Error reading file';
            setError(errorMessage);
            onError(errorMessage);
        } finally {
            setIsLoading(false);
        }
    };

    const clearFile = () => {
        setFile(null);
        setError(null);
    };

    return {
        file,
        isLoading,
        error,
        handleFileChange,
        clearFile,
    };
};

export default useFileUpload;

