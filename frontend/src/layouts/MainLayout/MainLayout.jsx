import React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import { useTheme } from '@mui/material/styles';

const MainLayout = ({ children }) => {
    const theme = useTheme();
    const currentYear = new Date().getFullYear();

    return (
        <Box sx={{
            display: 'flex',
            flexDirection: 'column',
            minHeight: '100vh',
            bgcolor: 'background.default'
        }}>
            <Container component="main" sx={{ flex: 1, py: 4 }}>
                {children}
            </Container>
            <Box
                component="footer"
                sx={{
                    py: 3,
                    bgcolor: 'primary.main',
                    color: 'primary.contrastText',
                    mt: 'auto',
                    textAlign: 'center'
                }}
            >
                <Typography variant="body2">
                    © {currentYear} File Analyzer
                </Typography>
            </Box>
        </Box>
    );
};

export default MainLayout;