/**
 * UI component mapping for consistent styling
 */

// Import theme configuration
import theme from './theme';

// Define reusable class mappings for common UI elements
export const ui = {
    // Layout elements
    container: 'container',
    row: 'row',
    column: 'column',

    // Interactive elements
    button: {
        primary: 'button',
        secondary: 'button button-secondary',
        small: 'button button-small',
        large: 'button button-large',
        link: 'button-link',
    },

    // Form elements
    input: 'input-field',
    select: 'select-field',
    checkbox: 'checkbox-field',
    radio: 'radio-field',

    // Content containers
    card: 'card',
    panel: 'panel',

    // Feedback elements
    alert: {
        info: 'alert alert-info',
        success: 'alert alert-success',
        warning: 'alert alert-warning',
        error: 'alert alert-error',
    },

    // Spacing utilities
    spacing: {
        marginTop: (size) => `mt-${size}`,
        marginBottom: (size) => `mb-${size}`,
        marginLeft: (size) => `ml-${size}`,
        marginRight: (size) => `mr-${size}`,
        paddingTop: (size) => `pt-${size}`,
        paddingBottom: (size) => `pb-${size}`,
        paddingLeft: (size) => `pl-${size}`,
        paddingRight: (size) => `pr-${size}`,
    }
};

export default ui;