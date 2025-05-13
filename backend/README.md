
# Backend API

FastAPI application for handling all backend operations.

## Structure

- `main.py` - Application entry point and configuration
- `auth.py` - Authentication and authorization
- `models/` - Pydantic schemas and database models
- `services/` - Business logic and external integrations
- `utils/` - Helper functions and utilities
- `tests/` - Unit and integration tests

## Adding New Endpoints

1. Create a new router file or use an existing one
2. Define your endpoint with appropriate HTTP method
3. Add request/response models using Pydantic
4. Implement the endpoint logic
5. Register the router in `main.py`

### Example: Creating a new router

```python
# src/routers/items.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.item import Item, ItemCreate
from ..services.items import ItemService
from ..auth import get_current_user

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[Item])
async def get_items(current_user = Depends(get_current_user)):
    return await ItemService.get_items(current_user.id)

@router.post("/", response_model=Item)
async def create_item(
    item: ItemCreate,
    current_user = Depends(get_current_user)
):
    return await ItemService.create_item(item, current_user.id)
```

Then register in main.py:

```python
from .routers import items

app.include_router(items.router)
```

## Best Practices

- Use dependency injection for services and database access
- Validate all inputs with Pydantic models
- Handle exceptions properly and return appropriate status codes
- Document all endpoints with docstrings
- Write tests for all endpoints