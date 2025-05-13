# Frontend Coding Standards

This document outlines the coding standards for our Next.js/React projects. Following these standards ensures code quality, readability, and maintainability.

## 1. Component Structure

### File Organization

Components should follow this structure:
```
ComponentName/
├── index.tsx         # Main export
├── ComponentName.tsx # Implementation
├── types.ts          # TypeScript interfaces/types
├── styles.ts         # Styled components (if applicable)
├── utils.ts          # Component-specific utilities
└── ComponentName.test.tsx  # Tests
```

### Directory Organization

Our frontend follows this directory structure:
```
frontend/src/
├── components/         # Reusable UI components
│   ├── common/         # Shared common components
│   └── features/       # Feature-specific components
├── configs/            # Configuration files
├── constants/          # Application constants
├── contexts/           # React context providers
├── external/           # External integrations
├── functions/          # Utility functions
├── helpers/            # Helper functions
├── hooks/              # Custom React hooks
├── interfaces/         # TypeScript interfaces
├── layouts/            # Page layout components
├── pages/              # Next.js pages and API routes
│   ├── auth/           # Authentication pages
│   ├── dashboard/      # Dashboard pages
├── services/           # API clients and service integrations
│   ├── api/            # API service
│   ├── auth/           # Authentication service
│   └── state/          # State management services
├── store/              # Global state management
├── styles/             # Global styles and theme configuration
├── types/              # TypeScript type definitions
└── utils/              # Utility functions and helpers
```

### Component Guidelines

- Use **functional components** with hooks
- Keep components **small and focused** on a single responsibility
- Use **PascalCase** for component names and files
- Extract complex logic into custom hooks
- Use TypeScript interfaces for props

### Example Component

```tsx
// GoodComponent.tsx
import React from 'react';
import { Box, Typography } from '@mui/material';
import { GoodComponentProps } from './types';
import { formatData } from './utils';

export function GoodComponent({ title, data, onAction }: GoodComponentProps) {
  const formattedData = formatData(data);

  return (
    <Box>
      <Typography variant="h6">{title}</Typography>
      {formattedData.map((item) => (
        <Box key={item.id} onClick={() => onAction(item.id)}>
          {item.label}
        </Box>
      ))}
    </Box>
  );
}
```

## 2. TypeScript Best Practices

### Types and Interfaces

- **Define interfaces** for all props
- Use **interfaces** for objects with methods or when you might need extension
- Use **type** for unions, intersections, or simple object shapes
- **Export types** that are used by multiple components
- Place shared types in the `/types` directory
- Place component-specific types in the component's directory

```typescript
// Good type definitions
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'guest';
}

type ButtonSize = 'small' | 'medium' | 'large';

interface ButtonProps {
  label: string;
  size?: ButtonSize;
  onClick: () => void;
  disabled?: boolean;
}
```

### Type Safety

- Avoid `any` type when possible
- Use type guards for runtime type checking
- Explicitly type function parameters and return values
- Use generics for reusable components and functions

## 3. State Management

### Local State

- Use `useState` for simple component state
- Use `useReducer` for complex state logic
- Keep state as close as possible to where it's used

### Global State

- Use the store directory for global state management
- Use context for sharing state across multiple components
- Create separate contexts for different domains (auth, theme, etc.)
- Provide meaningful default values for contexts

### Example Context Usage

```tsx
// Good context usage
import { useAuth } from '@/contexts/AuthContext';

function ProfileButton() {
  const { user, logout } = useAuth();

  if (!user) return null;

  return (
    <Button onClick={logout}>
      Logout {user.name}
    </Button>
  );
}
```

## 4. Hooks Guidelines

- Follow the [Rules of Hooks](https://reactjs.org/docs/hooks-rules.html)
- Create custom hooks to reuse stateful logic
- Keep hooks focused on specific functionality
- Name hooks with the `use` prefix
- Store reusable hooks in the `/hooks` directory

### Example Custom Hook

```typescript
// Good custom hook
import { useState, useEffect } from 'react';
import api from '@/services/api';

export function useData<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    let isMounted = true;

    async function fetchData() {
      try {
        setLoading(true);
        const response = await api.get<T>(url);
        if (isMounted) {
          setData(response.data);
          setError(null);
        }
      } catch (err) {
        if (isMounted && err instanceof Error) {
          setError(err);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    fetchData();

    return () => {
      isMounted = false;
    };
  }, [url]);

  return { data, loading, error };
}
```

## 5. API Integration

- Use the centralized API service in `/services/api` for all requests
- Handle loading and error states
- Use TypeScript interfaces for request/response types
- Implement proper error handling

```typescript
// Good API integration
import { useState } from 'react';
import api from '@/services/api';
import { User } from '@/types/user';

export function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function fetchUser() {
    setLoading(true);
    setError(null);
    try {
      const response = await api.get<User>(`/users/${userId}`);
      setUser(response.data);
    } catch (err) {
      setError('Failed to load user profile');
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  // Component implementation
}
```

## 6. Styling

- Use Material UI's styling system
- Use theme variables instead of hardcoded values
- Keep styles close to the components that use them
- Use responsive design principles
- Store global styles in the `/styles` directory

### Theme Usage

```typescript
// Good theme usage
import { Box, Typography } from '@mui/material';

function ThemedComponent() {
  return (
    <Box
      sx={{
        bgcolor: 'background.paper',
        borderRadius: 1,
        p: 2,
        '&:hover': {
          bgcolor: 'action.hover',
        },
        [theme => theme.breakpoints.down('md')]: {
          p: 1,
        }
      }}
    >
      <Typography color="primary.main" variant="h6">
        Themed Content
      </Typography>
    </Box>
  );
}
```

## 7. Testing

- Write tests for all components
- Test component rendering, interactions, and state changes
- Use meaningful test descriptions
- Mock external dependencies
- Place tests alongside the components they test

### Example Test

```typescript
// Good test
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button component', () => {
  test('renders with correct label', () => {
    render(<Button label="Click me" onClick={() => {}} />);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  test('calls onClick when clicked', () => {
    const handleClick = jest.fn();
    render(<Button label="Click me" onClick={handleClick} />);
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  test('is disabled when disabled prop is true', () => {
    render(<Button label="Click me" onClick={() => {}} disabled />);
    expect(screen.getByText('Click me')).toBeDisabled();
  });
});
```

## 8. Performance Optimization

- Use `React.memo()` for expensive components
- Optimize re-renders with `useCallback` and `useMemo`
- Use virtualization for long lists
- Implement code splitting with dynamic imports

### Example Performance Optimization

```typescript
// Good performance optimization
import React, { useCallback, useMemo } from 'react';

const ExpensiveComponent = React.memo(function ExpensiveComponent({ data, onItemClick }) {
  // Component implementation
});

function ParentComponent({ items }) {
  // Memoize expensive calculations
  const processedData = useMemo(() => {
    return items.map(item => ({
      ...item,
      processed: expensiveOperation(item)
    }));
  }, [items]);

  // Memoize callback functions
  const handleItemClick = useCallback((id) => {
    console.log(`Item ${id} clicked`);
  }, []);

  return (
    <ExpensiveComponent
      data={processedData}
      onItemClick={handleItemClick}
    />
  );
}
```

## 9. Project Organization

- Follow the established directory structure
- Place components in the appropriate subdirectory:
  - `common/` for shared components
  - `features/` for feature-specific components
- Keep related files together
- Use appropriate naming conventions for files and directories