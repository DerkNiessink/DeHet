import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        mode: 'light',
        primary: {
            main: '#232F34',         // Deep dark blue-gray
            contrastText: '#FFFFFF',
        },
        secondary: {
            main: '#F9AA33',         // Reply orange
            contrastText: '#000000',
        },
        background: {
            default: '#FFFFFF',      // Light background
            paper: '#FFFFFF',        // Cards, etc.
        },
        text: {
            primary: '#344955',      // Text headings
            secondary: '#4A6572',    // Secondary text
        },
        divider: '#E0E0E0',        // Optional soft border
    },

    typography: {
        fontFamily: [
            'Segoe UI',
            'Roboto',
            '"Helvetica Neue"',
            'Arial',
            'sans-serif',
        ].join(','),
        h1: {
            fontWeight: 700,
            fontSize: '2.25rem',
            color: '#344955',
        },
        h2: {
            fontWeight: 600,
            fontSize: '1.75rem',
            color: '#4A6572',
        },
        h3: {
            fontWeight: 500,
            fontSize: '1.5rem',
            color: '#344955',
        },
        body1: {
            color: '#4A6572',
        },
        button: {
            fontWeight: 600,
            textTransform: 'none',
        },
    },

    shape: {
        borderRadius: 10,
    },

    shadows: [
        'none',
        '0px 2px 1px -1px rgba(52, 73, 85, 0.1),0px 1px 1px 0px rgba(52, 73, 85, 0.07),0px 1px 3px 0px rgba(52, 73, 85, 0.06)',
        ...Array(23).fill('0px 4px 6px rgba(52, 73, 85, 0.1)'),
    ],

    components: {
        MuiButton: {
            styleOverrides: {
                root: {
                    backgroundColor: '#F9AA33',
                    color: '#000',
                    textTransform: 'none',
                    fontWeight: 600,
                    borderRadius: 50, // For FAB look
                    padding: '10px 20px',
                    boxShadow: '0 4px 8px rgba(249, 170, 51, 0.3)',
                    '&:hover': {
                        backgroundColor: '#e0902d',
                        boxShadow: '0 6px 12px rgba(249, 170, 51, 0.35)',
                    },
                },
            },
        },

        MuiPaper: {
            styleOverrides: {
                root: {
                    backgroundColor: '#ffffff',
                    border: '1px solid #E0E0E0',
                    borderRadius: 12,
                    padding: '16px',
                    boxShadow: '0 2px 4px rgba(52, 73, 85, 0.1)',
                },
            },
        },

        MuiAppBar: {
            styleOverrides: {
                root: {
                    backgroundColor: '#344955',
                    color: '#ffffff',
                },
            },
        },

        MuiCssBaseline: {
            styleOverrides: {
                body: {
                    backgroundColor: '#FFFFFF',
                },
            },
        },
    },
});

export default theme;