# Backend Coding Standards

This document outlines the coding standards for our FastAPI Python projects. Following these standards ensures code quality, readability, and maintainability.

## 1. Project Structure

Our FastAPI applications follow this structure:

```
backend/
├── src/
│   ├── main.py           # Application entry point
│   ├── models/           # Pydantic schemas and database models
│   ├── routers/          # API route handlers
│   ├── services/         # Business logic
│   ├── utils/            # Helper functions
│   └── tests/            # Unit and integration tests
├── requirements.txt      # Dependencies
├── pytest.ini           # Test configuration
└── .env                 # Environment variables (not in git)
```

## 2. API Design

### Routing

- Group related endpoints in router modules
- Use meaningful route paths
- Follow REST principles
- Use plural nouns for resources (e.g., `/users`, `/documents`)
- Include version in API path (e.g., `/api/v1/users`)

```python
# Good routing example
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.get("/")
async def get_users():
    # Implementation

@router.get("/{user_id}")
async def get_user(user_id: str):
    # Implementation
```

### Request Validation

- Use Pydantic models for request/response validation
- Define clear, specific models for each endpoint
- Document models with docstrings
- Include field validations

```python
# Good validation example
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    """User creation model."""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "full_name": "John Doe"
            }
        }
```

### Response Structure

- Return consistent response structures
- Use appropriate status codes
- Handle errors with meaningful messages

```python
# Good response example
from fastapi import HTTPException, status
from typing import List

@router.get("/", response_model=List[UserResponse])
async def get_users():
    users = await user_service.get_users()
    return users

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user
```

## 3. Authentication & Security

- Store passwords with proper hashing (bcrypt)
- Use JWT for authentication
- Implement proper token validation
- Use dependency injection for auth requirements

```python
# Good authentication example
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user
```

## 4. Business Logic

- Keep business logic in service modules
- Separate concerns by domain
- Use dependency injection for services
- Handle errors appropriately

```python
# Good service example
from fastapi import Depends
from .database import get_db

class UserService:
    def __init__(self, db = Depends(get_db)):
        self.db = db

    async def get_user(self, user_id: str):
        """Get user by ID."""
        return await self.db.users.find_one({"_id": user_id})

    async def create_user(self, user: UserCreate):
        """Create a new user."""
        # Check if email already exists
        existing_user = await self.db.users.find_one({"email": user.email})
        if existing_user:
            return None

        # Hash password
        hashed_password = get_password_hash(user.password)

        # Create user document
        user_data = user.dict()
        user_data["password"] = hashed_password
        user_data["created_at"] = datetime.utcnow()

        result = await self.db.users.insert_one(user_data)
        return await self.get_user(result.inserted_id)
```

## 5. Database Interactions

- Use async database clients when possible
- Implement proper connection pooling
- Handle database exceptions
- Use transactions for multi-step operations

```python
# Good database interaction
async def create_order_with_items(order_data, item_data_list):
    async with db.transaction():
        try:
            # Create order
            order_id = await db.orders.insert_one(order_data)

            # Create all items with order reference
            items = [
                {**item, "order_id": order_id}
                for item in item_data_list
            ]
            await db.order_items.insert_many(items)

            return order_id
        except Exception as e:
            # Transaction will automatically roll back
            logger.error(f"Failed to create order: {e}")
            raise
```

## 6. Error Handling

- Use appropriate exception types
- Provide meaningful error messages
- Include error codes
- Log exceptions appropriately

```python
# Good error handling
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, current_user = Depends(get_current_user)):
    try:
        result = await item_service.create_item(item, current_user.id)
        return result
    except ValueError as e:
        # Client error
        raise HTTPException(status_code=400, detail=str(e))
    except PermissionError as e:
        # Authorization error
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        # Unexpected error
        error_id = generate_error_id()
        logger.error(f"Error {error_id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred. Reference: {error_id}"
        )
```

## 7. Testing

- Write unit tests for models, services, and utilities
- Write API tests for endpoints
- Use pytest fixtures for common test setup
- Mock external dependencies

### Example Test

```python
# Good test example
import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_user_service():
    return MagicMock()

@pytest.fixture
def client(mock_user_service):
    with patch("app.dependencies.get_user_service", return_value=mock_user_service):
        from app.main import app
        with TestClient(app) as client:
            yield client

def test_get_user(client, mock_user_service):
    # Setup mock
    mock_user = {"id": "user1", "username": "testuser", "email": "test@example.com"}
    mock_user_service.get_user.return_value = mock_user

    # Execute request
    response = client.get("/api/v1/users/user1")

    # Assertions
    assert response.status_code == 200
    assert response.json() == mock_user
    mock_user_service.get_user.assert_called_once_with("user1")

def test_get_user_not_found(client, mock_user_service):
    # Setup mock
    mock_user_service.get_user.return_value = None

    # Execute request
    response = client.get("/api/v1/users/nonexistent")

    # Assertions
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
```

## 8. Async Programming

- Use async/await for IO-bound operations
- Avoid blocking the event loop
- Use proper concurrency patterns

```python
# Good async example
import asyncio
from typing import List

async def fetch_item(item_id: str):
    # Async IO operation
    return await db.items.find_one({"_id": item_id})

@router.get("/batch", response_model=List[ItemResponse])
async def get_items_batch(item_ids: List[str]):
    # Fetch multiple items concurrently
    items = await asyncio.gather(*[
        fetch_item(item_id) for item_id in item_ids
    ])
    return [item for item in items if item is not None]
```

## 9. Logging

- Use structured logging
- Include contextual information
- Configure appropriate log levels
- Log important application events

```python
# Good logging example
import logging
import uuid
from fastapi import Request

logger = logging.getLogger(__name__)

async def log_request_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    logger.info(
        f"Request started",
        extra={
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "client_ip": request.client.host
        }
    )

    try:
        response = await call_next(request)
        logger.info(
            f"Request completed",
            extra={
                "request_id": request_id,
                "status_code": response.status_code
            }
        )
        return response
    except Exception as e:
        logger.error(
            f"Request failed",
            extra={
                "request_id": request_id,
                "error": str(e)
            },
            exc_info=True
        )
        raise
```

## 10. Performance

- Use async for IO-bound operations
- Implement proper caching
- Optimize database queries
- Monitor and profile endpoints

```python
# Good performance example
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

@router.get("/popular-items", response_model=List[ItemResponse])
@cache(expire=300)  # Cache for 5 minutes
async def get_popular_items():
    # This expensive operation will be cached
    items = await item_service.get_popular_items()
    return items
```
