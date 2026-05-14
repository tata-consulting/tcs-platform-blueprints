from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import ExampleItem, ExampleResponse

router = APIRouter()


# Example dependency - replace with real DB session or service client
def get_service():
    """Dependency injection example. Replace with actual service/session factory."""
    return {"connected": True}


ServiceDep = Annotated[dict, Depends(get_service)]


@router.get("/items/{item_id}", response_model=ExampleResponse)
async def get_item(item_id: int, service: ServiceDep) -> ExampleResponse:
    """Retrieve an item by ID.

    Replace this with your actual business logic.
    """
    return ExampleResponse(
        id=item_id,
        name=f"Example item {item_id}",
        description="Replace with real data",
    )


@router.post("/items", response_model=ExampleResponse, status_code=201)
async def create_item(item: ExampleItem, service: ServiceDep) -> ExampleResponse:
    """Create a new item.

    Replace this with your actual business logic.
    """
    return ExampleResponse(
        id=1,
        name=item.name,
        description=item.description,
    )
