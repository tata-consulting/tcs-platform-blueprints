from pydantic import BaseModel, Field


class ExampleItem(BaseModel):
    """Request model for creating an item. Replace with your domain model."""

    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: str | None = Field(None, max_length=500, description="Optional description")


class ExampleResponse(BaseModel):
    """Response model for an item. Replace with your domain model."""

    id: int = Field(..., description="Unique identifier")
    name: str = Field(..., description="Item name")
    description: str | None = Field(None, description="Optional description")

    model_config = {"from_attributes": True}
