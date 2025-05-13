import React, { useState } from 'react';
import { Button, Box, Typography, CircularProgress, Alert } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import FileUploadIcon from '@mui/icons-material/FileUpload';
import { styled } from '@mui/material/styles';

const VisuallyHiddenInput = styled('input')({
    clip: 'rect(0 0 0 0)',
    clipPath: 'inset(50%)',
    height: 1,
    overflow: 'hidden',
    position: 'absolute',
    bottom: 0,
    left: 0,
    whiteSpace: 'nowrap',
    width: 1,
});

const FileUpload = ({ onFileChange, isLoading = false, error = null, acceptedTypes = ['ics'] }) => {
    const [fileName, setFileName] = useState('');
    const [localError, setLocalError] = useState('');

    const handleChange = (event) => {
        const file = event.target.files[0];

        if (file && file.name.endsWith('.ics')) {
            setFileName(file.name);
            setLocalError('');
            if (onFileChange) onFileChange(event);
        } else {
            setFileName('');
            setLocalError('Only .ics files are allowed.');
            if (onFileChange) onFileChange(null);
        }
    };



    const acceptedFileTypes = '.ics'



    return (
        <Box sx={{ width: '100%', maxWidth: 500, textAlign: 'center' }}>
            <Button
                component="label"
                variant="contained"
                startIcon={isLoading ? <CircularProgress size={20} color="inherit" /> : <CloudUploadIcon />}
                disabled={isLoading}
                sx={{ mb: 2, py: 1.5, px: 3 }}
            >
                {isLoading ? 'Processing...' : 'Upload File'}
                <VisuallyHiddenInput
                    type="file"
                    onChange={handleChange}
                    accept={acceptedFileTypes}
                    disabled={isLoading}
                />
            </Button>

            {fileName && (
                <Typography variant="body2" sx={{ fontStyle: 'italic', color: 'primary.dark', mt: 1 }}>
                    <FileUploadIcon fontSize="small" sx={{ verticalAlign: 'middle', mr: 0.5 }} />
                    {fileName}
                </Typography>
            )}

            {(error || localError) && (
                <Alert severity="error" sx={{ mt: 2 }}>
                    {error || localError}
                </Alert>
            )}


            {acceptedTypes.length > 0 && (
                <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block' }}>
                    Accepted file types: {acceptedFileTypes}
                </Typography>
            )}
        </Box>
    );
};

export default FileUpload;