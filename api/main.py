"""FastAPI application with task history endpoint."""
from fastapi import FastAPI, Query
from typing import Optional

from api.models import get_all_tasks, Task

app = FastAPI(
    title="Entangled with the Word API",
    description="API for task management and spiritual reflections",
    version="1.0.0",
)


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Welcome to Entangled with the Word API"}


@app.get("/tasks", response_model=list[Task])
def get_tasks(
    status: Optional[str] = Query(None, description="Filter tasks by status"),
    tag: Optional[str] = Query(None, description="Filter tasks by tag"),
):
    """
    Get task history.

    Returns a list of all tasks, optionally filtered by status or tag.
    """
    tasks = get_all_tasks()

    # Apply filters if provided
    if status:
        tasks = [t for t in tasks if t.get("status") == status]
    if tag:
        tasks = [t for t in tasks if t.get("tag") == tag]

    return tasks
