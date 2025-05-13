import React from 'react';
import { Paper, Typography, Box } from '@mui/material';
import { styled } from '@mui/material/styles';

const OutputContent = styled(Box)(({ theme }) => ({
    minHeight: 200,
    padding: theme.spacing(2),
    backgroundColor: theme.palette.grey[50],
    borderRadius: theme.shape.borderRadius,
    fontFamily: 'monospace',
    whiteSpace: 'pre-wrap',
    wordBreak: 'break-word',
    border: `1px solid ${theme.palette.primary.light}`,
    overflowY: 'auto',
    maxHeight: 500,
}));

const OutputBox = ({ content }) => {
    return (
        <Paper
            elevation={2}
            sx={{
                width: '100%',
                maxWidth: 800,
                p: 3,
                border: (theme) => `2px solid ${theme.palette.primary.light}`,
                borderRadius: 2,
            }}
        >
            <Typography
                variant="h2"
                component="h2"
                gutterBottom
                sx={{
                    pb: 1,
                    borderBottom: (theme) => `2px solid ${theme.palette.primary.light}`,
                }}
            >
                Results
            </Typography>

            <OutputContent>
                {content || 'Upload a file to see results here'}
            </OutputContent>
        </Paper>
    );
};

export default OutputBox;