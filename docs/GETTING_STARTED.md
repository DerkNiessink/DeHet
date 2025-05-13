# Getting Started

This guide will help you set up your development environment and make your first contribution to the boilerplate project.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Node.js](https://nodejs.org/) v16+ (optional for local development)
- [Python](https://www.python.org/) v3.9+ (optional for local development)
- A code editor (we recommend [VS Code](https://code.visualstudio.com/))

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/prototype-boilerplate.git
cd prototype-boilerplate
```

## Step 2: Environment Setup

### Docker Development (Recommended)

The easiest way to get started is using Docker:

1. Create a copy of the example environment files:

```bash
# For frontend
cp frontend/.env.example frontend/.env.local

# For backend
cp backend/.env.example backend/.env
```

2. Start the development environment:

```bash
docker-compose -f docker-compose.dev.yml up
```

This will:
- Start the frontend on http://localhost:3000
- Start the backend on http://localhost:8000
- Set up hot-reloading for both

### Local Development (Alternative)

If you prefer to develop locally:

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at http://localhost:3000

#### Backend Setup

```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

The backend API will be available at http://localhost:8000

## Step 3: Project Structure

Take some time to explore the project structure:

### Frontend Structure

```
frontend/src/
├── components/         # Reusable UI components
│   ├── common/         # Shared common components
│   ├── examples/       # Example components for demonstration
│   │   ├── ai/         # AI-related example components
│   │   ├── data/       # Data visualization example components
│   │   └── ui/         # UI example components
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
│   └── examples/       # Example pages
├── services/           # API clients and service integrations
│   ├── api/            # API service
│   ├── auth/           # Authentication service
│   ├── examples/       # Example services
│   └── state/          # State management services
├── store/              # Global state management
├── styles/             # Global styles and theme configuration
├── types/              # TypeScript type definitions
└── utils/              # Utility functions and helpers
```

### Backend Structure

```
backend/src/
├── main.py          # Application entry point
├── auth.py          # Authentication logic
├── models/          # Data models
├── services/        # Business logic
├── utils/           # Utility functions
└── tests/           # Unit and integration tests
```

## Step 4: Make Your First Change

Let's make a simple change to verify everything is working:

### Frontend Change

1. Open `frontend/src/pages/index.tsx`
2. Modify the welcome message
3. Save the file and see the change in your browser

### Backend Change

1. Open `backend/src/main.py`
2. Add a new endpoint:

```python
@app.get("/hello")
async def hello():
    return {"message": "Hello World!"}
```

3. Save the file
4. Test your endpoint by visiting http://localhost:8000/hello

## Step 5: Running Tests

It's important to run tests before submitting changes:

### Frontend Tests

```bash
cd frontend
npm test
```

### Backend Tests

```bash
cd backend
pytest
```

## Step 6: Best Practices

Follow these guidelines when developing:

1. **Code Style**: Follow the established code style (enforced by ESLint/Prettier)
2. **Component Structure**: Follow the component structure in our [Frontend Coding Standards](./FRONTEND_STANDARDS.md)
3. **State Management**: Use React Context for global state
4. **API Integration**: Use the API service for all requests
5. **Testing**: Write tests for new components and functions
6. **Documentation**: Add JSDoc/docstring comments to your code

## Troubleshooting

### Common Issues

#### Docker Issues

- **Port conflicts**: If you see "port is already allocated", stop other services using those ports
- **Permission errors**: You might need to run Docker commands with sudo on Linux

#### Frontend Issues

- **Module not found**: Try `npm install` to install missing dependencies
- **Build errors**: Check for TypeScript errors in your code

#### Backend Issues

- **Import errors**: Make sure your virtual environment is activated
- **Database errors**: Check your database connection settings

### Getting Help

If you're stuck:

1. Check our [internal documentation](./docs)
2. Ask in the team Slack channel
3. Open an issue on our internal GitHub repository
4. Ask Claude or GPT

Happy coding!