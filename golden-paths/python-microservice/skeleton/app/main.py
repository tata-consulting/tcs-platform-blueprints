from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routers import example


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialize connections, load models, etc.
    yield
    # Shutdown: close connections, flush buffers, etc.


app = FastAPI(
    title="${{ values.name }}",
    description="${{ values.description }}",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(example.router, prefix="/api/v1", tags=["example"])


@app.get("/health", tags=["health"])
async def health() -> dict:
    """Health check endpoint for liveness and readiness probes."""
    return {"status": "ok"}
