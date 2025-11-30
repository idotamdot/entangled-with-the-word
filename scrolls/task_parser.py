# scrolls/task_parser.py
"""
Task parser module for extracting tags and due dates from task input text.
Connects to SQLite database for persistent storage.
"""

import re
import sqlite3
import os
from datetime import datetime, timedelta
from typing import Optional
from dataclasses import dataclass

from scrolls.categories import PROJECT_CATEGORIES

# Database configuration
DB_DIR = "data"
DB_FILE = os.path.join(DB_DIR, "tasks.db")

# Track whether database has been initialized
_db_initialized = False


@dataclass
class ParsedTask:
    """Represents a parsed task with extracted components."""
    original_text: str
    description: str
    tags: list[str]
    due_date: Optional[datetime]


def parse_tags(text: str) -> list[str]:
    """
    Extract hashtags from input text.
    Returns list of tags found (including the # symbol).
    
    Examples:
        "Meeting tomorrow #Projects" -> ["#Projects"]
        "Fix bug #Timeline #Quantum" -> ["#Timeline", "#Quantum"]
    """
    # Match hashtags (# followed by word characters)
    pattern = r'#\w+'
    found_tags = re.findall(pattern, text)
    
    # Validate against known categories, keep all found tags
    validated_tags = []
    for tag in found_tags:
        # Normalize case for matching
        matched = False
        for category in PROJECT_CATEGORIES:
            if tag.lower() == category.lower():
                validated_tags.append(category)  # Use canonical form
                matched = True
                break
        if not matched:
            validated_tags.append(tag)  # Keep unknown tags as-is
    
    return validated_tags


def parse_due_date(text: str) -> Optional[datetime]:
    """
    Extract due date from input text.
    Supports formats:
        - due:YYYY-MM-DD (e.g., due:2025-12-01)
        - due:MM/DD/YYYY (e.g., due:12/01/2025)
        - due:tomorrow
        - due:next week
        - due:today
    
    Returns datetime object or None if no due date found.
    """
    # Pattern matches: due: followed by non-whitespace, optionally followed by
    # a space and another word (to capture "next week" style patterns)
    due_pattern = r'due:(\S+(?:\s+\w+)?)'
    match = re.search(due_pattern, text, re.IGNORECASE)
    
    if not match:
        return None
    
    date_str = match.group(1).strip().lower()
    today = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)
    
    # Handle relative dates
    if date_str == 'today':
        return today
    elif date_str == 'tomorrow':
        return today + timedelta(days=1)
    elif date_str.startswith('next'):
        # Handle "next week"
        if 'week' in date_str:
            return today + timedelta(weeks=1)
        return None
    
    # Try parsing absolute dates
    date_formats = [
        '%Y-%m-%d',      # 2025-12-01
        '%m/%d/%Y',      # 12/01/2025
        '%d/%m/%Y',      # 01/12/2025
        '%Y/%m/%d',      # 2025/12/01
    ]
    
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    return None


def extract_description(text: str) -> str:
    """
    Extract the task description by removing tags and due date specifications.
    """
    # Remove hashtags
    description = re.sub(r'#\w+', '', text)
    # Remove due: specifications using the same pattern as parse_due_date
    # This ensures consistency between parsing and extraction
    description = re.sub(r'due:\S+(?:\s+week)?', '', description, flags=re.IGNORECASE)
    # Clean up extra whitespace
    description = ' '.join(description.split())
    return description.strip()


def parse_task(text: str) -> ParsedTask:
    """
    Parse a task input string and extract all components.
    
    Args:
        text: Raw task input string
        
    Returns:
        ParsedTask object with extracted components
    """
    tags = parse_tags(text)
    due_date = parse_due_date(text)
    description = extract_description(text)
    
    return ParsedTask(
        original_text=text,
        description=description,
        tags=tags,
        due_date=due_date
    )


# ============ Database Functions ============

def _ensure_db_initialized() -> None:
    """Ensure database is initialized (called once per process)."""
    global _db_initialized
    if not _db_initialized:
        init_database()
        _db_initialized = True


def init_database() -> None:
    """Initialize the SQLite database and create tables if they don't exist."""
    os.makedirs(DB_DIR, exist_ok=True)
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT,
            created_at TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    ''')
    
    # Create tags table for many-to-many relationship
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS task_tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            tag TEXT NOT NULL,
            FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE
        )
    ''')
    
    # Create index for faster tag lookups
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_task_tags_task_id ON task_tags (task_id)
    ''')
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_task_tags_tag ON task_tags (tag)
    ''')
    
    conn.commit()
    conn.close()


def save_task(parsed_task: ParsedTask) -> int:
    """
    Save a parsed task to the database.
    
    Args:
        parsed_task: ParsedTask object to save
        
    Returns:
        The ID of the newly created task
    """
    _ensure_db_initialized()
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Insert the task
    due_date_str = parsed_task.due_date.isoformat() if parsed_task.due_date else None
    created_at = datetime.now().isoformat()
    
    cursor.execute('''
        INSERT INTO tasks (original_text, description, due_date, created_at)
        VALUES (?, ?, ?, ?)
    ''', (parsed_task.original_text, parsed_task.description, due_date_str, created_at))
    
    task_id = cursor.lastrowid
    
    # Insert tags
    for tag in parsed_task.tags:
        cursor.execute('''
            INSERT INTO task_tags (task_id, tag)
            VALUES (?, ?)
        ''', (task_id, tag))
    
    conn.commit()
    conn.close()
    
    return task_id


def get_task(task_id: int) -> Optional[dict]:
    """
    Retrieve a task by ID from the database.
    
    Returns:
        Dictionary with task data or None if not found
    """
    _ensure_db_initialized()
    
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        return None
    
    task = dict(row)
    
    # Get associated tags
    cursor.execute('SELECT tag FROM task_tags WHERE task_id = ?', (task_id,))
    task['tags'] = [r['tag'] for r in cursor.fetchall()]
    
    conn.close()
    return task


def get_all_tasks(include_completed: bool = True) -> list[dict]:
    """
    Retrieve all tasks from the database.
    
    Args:
        include_completed: Whether to include completed tasks
        
    Returns:
        List of task dictionaries
    """
    _ensure_db_initialized()
    
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if include_completed:
        cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
    else:
        cursor.execute('SELECT * FROM tasks WHERE completed = 0 ORDER BY created_at DESC')
    
    rows = cursor.fetchall()
    tasks = []
    
    for row in rows:
        task = dict(row)
        cursor.execute('SELECT tag FROM task_tags WHERE task_id = ?', (task['id'],))
        task['tags'] = [r['tag'] for r in cursor.fetchall()]
        tasks.append(task)
    
    conn.close()
    return tasks


def get_tasks_by_tag(tag: str) -> list[dict]:
    """
    Retrieve all tasks with a specific tag.
    
    Args:
        tag: The tag to filter by
        
    Returns:
        List of task dictionaries
    """
    _ensure_db_initialized()
    
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT DISTINCT t.* FROM tasks t
        INNER JOIN task_tags tt ON t.id = tt.task_id
        WHERE tt.tag = ?
        ORDER BY t.created_at DESC
    ''', (tag,))
    
    rows = cursor.fetchall()
    tasks = []
    
    for row in rows:
        task = dict(row)
        cursor.execute('SELECT tag FROM task_tags WHERE task_id = ?', (task['id'],))
        task['tags'] = [r['tag'] for r in cursor.fetchall()]
        tasks.append(task)
    
    conn.close()
    return tasks


def mark_task_completed(task_id: int, completed: bool = True) -> bool:
    """
    Mark a task as completed or incomplete.
    
    Returns:
        True if task was found and updated, False otherwise
    """
    _ensure_db_initialized()
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE tasks SET completed = ? WHERE id = ?
    ''', (1 if completed else 0, task_id))
    
    updated = cursor.rowcount > 0
    conn.commit()
    conn.close()
    
    return updated


def delete_task(task_id: int) -> bool:
    """
    Delete a task from the database.
    
    Returns:
        True if task was deleted, False otherwise
    """
    _ensure_db_initialized()
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Delete associated tags first
    cursor.execute('DELETE FROM task_tags WHERE task_id = ?', (task_id,))
    # Delete the task
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    
    return deleted


def parse_and_save_task(text: str) -> tuple[ParsedTask, int]:
    """
    Convenience function to parse a task and save it in one step.
    
    Args:
        text: Raw task input string
        
    Returns:
        Tuple of (ParsedTask, task_id)
    """
    parsed = parse_task(text)
    task_id = save_task(parsed)
    return parsed, task_id
