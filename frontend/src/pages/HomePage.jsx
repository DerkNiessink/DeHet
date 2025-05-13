import React, { useState } from 'react';
import { Container, Typography, Box } from '@mui/material';
import FileUpload from '../components/common/FileUpload/FileUpload';
import OutputBox from '../components/common/OutputBox/OutputBox';
import useFileUpload from '../hooks/useFileUpload';
import config from '../configs/app.config';

const HomePage = () => {
    const [outputText, setOutputText] = useState('');

    const { handleFileChange, isLoading, error } = useFileUpload({
        onSuccess: (content) => {
            setOutputText(content);
        },
        acceptedTypes: config.upload.acceptedFileTypes,
    });

    return (
        <Container maxWidth="md">
            <Box sx={{ my: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4 }}>
                <Typography variant="h1" component="h1" align="center">
                    {config.app.name}
                </Typography>
                <Typography variant="body1" align="center">
                    Upload two or more .ics files and we’ll spot the sweet spot.
                </Typography>

                <FileUpload
                    onFileChange={handleFileChange}
                    isLoading={isLoading}
                    error={error}
                    acceptedTypes={config.upload.acceptedFileTypes}
                />

                <OutputBox content={outputText} />
            </Box>
        </Container>
    );
};

export default HomePage;
