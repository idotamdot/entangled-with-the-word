"""Task model and data operations."""
import os
from datetime import datetime
from typing import Optional
import pandas as pd
from pydantic import BaseModel


class Task(BaseModel):
    """Model representing a task."""
    id: int
    title: str
    description: Optional[str] = None
    tag: Optional[str] = None
    due_date: Optional[str] = None
    status: str = "pending"
    created_at: str


TASKS_FILE = os.path.join("data", "tasks.csv")
TASKS_COLUMNS = ["id", "title", "description", "tag", "due_date", "status", "created_at"]


def get_tasks_file_path() -> str:
    """Return the path to the tasks CSV file."""
    return TASKS_FILE


def load_tasks() -> pd.DataFrame:
    """Load tasks from CSV file."""
    if not os.path.exists(TASKS_FILE):
        return pd.DataFrame(columns=TASKS_COLUMNS)
    try:
        df = pd.read_csv(TASKS_FILE)
        # Ensure all required columns exist
        for col in TASKS_COLUMNS:
            if col not in df.columns:
                df[col] = None if col != "status" else "pending"
        return df[TASKS_COLUMNS]
    except (pd.errors.EmptyDataError, pd.errors.ParserError, FileNotFoundError):
        return pd.DataFrame(columns=TASKS_COLUMNS)


def save_tasks(df: pd.DataFrame) -> None:
    """Save tasks to CSV file."""
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    df.to_csv(TASKS_FILE, index=False)


def get_all_tasks() -> list[dict]:
    """Get all tasks as a list of dictionaries."""
    df = load_tasks()
    if df.empty:
        return []
    # Convert to records and replace NaN with None for JSON serialization
    records = df.to_dict(orient="records")
    for record in records:
        for key, value in record.items():
            if pd.isna(value):
                record[key] = None
    return records


def create_task(
    title: str,
    description: Optional[str] = None,
    tag: Optional[str] = None,
    due_date: Optional[str] = None,
) -> dict:
    """Create a new task and save it."""
    df = load_tasks()
    if df.empty:
        new_id = 1
    else:
        # Safely convert ID column to numeric and get max
        numeric_ids = pd.to_numeric(df["id"], errors="coerce")
        max_id = numeric_ids.max()
        new_id = 1 if pd.isna(max_id) else int(max_id) + 1
    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "tag": tag,
        "due_date": due_date,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
    }
    df = pd.concat([df, pd.DataFrame([new_task])], ignore_index=True)
    save_tasks(df)
    return new_task
