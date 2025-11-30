# tests/test_task_parser.py
"""Tests for the task parser module."""

import os
import sys
import unittest
from datetime import datetime, timedelta

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrolls.task_parser import (
    parse_task,
    parse_tags,
    parse_due_date,
    extract_description,
    init_database,
    save_task,
    get_task,
    get_all_tasks,
    get_tasks_by_tag,
    mark_task_completed,
    delete_task,
    parse_and_save_task,
    ParsedTask,
    DB_FILE,
)


class TestParseTags(unittest.TestCase):
    """Test cases for tag parsing."""
    
    def test_parse_single_tag(self):
        """Test parsing a single tag."""
        result = parse_tags("Complete the project #Projects")
        self.assertEqual(result, ["#Projects"])
    
    def test_parse_multiple_tags(self):
        """Test parsing multiple tags."""
        result = parse_tags("Meditation time #Personal #Reflection")
        self.assertEqual(len(result), 2)
        self.assertIn("#Personal", result)
        self.assertIn("#Reflection", result)
    
    def test_parse_no_tags(self):
        """Test parsing text with no tags."""
        result = parse_tags("Complete the project without tags")
        self.assertEqual(result, [])
    
    def test_parse_unknown_tags(self):
        """Test parsing unknown tags (not in PROJECT_CATEGORIES)."""
        result = parse_tags("Task with #CustomTag")
        self.assertEqual(result, ["#CustomTag"])
    
    def test_parse_case_insensitive(self):
        """Test that tag matching is case-insensitive."""
        result = parse_tags("Task #projects #TIMELINE")
        self.assertIn("#Projects", result)
        self.assertIn("#Timeline", result)


class TestParseDueDate(unittest.TestCase):
    """Test cases for due date parsing."""
    
    def test_parse_due_today(self):
        """Test parsing 'due:today'."""
        result = parse_due_date("Task due:today")
        self.assertIsNotNone(result)
        self.assertEqual(result.date(), datetime.now().date())
    
    def test_parse_due_tomorrow(self):
        """Test parsing 'due:tomorrow'."""
        result = parse_due_date("Task due:tomorrow")
        tomorrow = datetime.now() + timedelta(days=1)
        self.assertIsNotNone(result)
        self.assertEqual(result.date(), tomorrow.date())
    
    def test_parse_due_next_week(self):
        """Test parsing 'due:next week'."""
        result = parse_due_date("Task due:next week")
        next_week = datetime.now() + timedelta(weeks=1)
        self.assertIsNotNone(result)
        self.assertEqual(result.date(), next_week.date())
    
    def test_parse_due_iso_format(self):
        """Test parsing ISO date format (YYYY-MM-DD)."""
        result = parse_due_date("Task due:2025-12-25")
        self.assertIsNotNone(result)
        self.assertEqual(result.year, 2025)
        self.assertEqual(result.month, 12)
        self.assertEqual(result.day, 25)
    
    def test_parse_due_us_format(self):
        """Test parsing US date format (MM/DD/YYYY)."""
        result = parse_due_date("Task due:12/25/2025")
        self.assertIsNotNone(result)
        self.assertEqual(result.year, 2025)
        self.assertEqual(result.month, 12)
        self.assertEqual(result.day, 25)
    
    def test_parse_no_due_date(self):
        """Test parsing text with no due date."""
        result = parse_due_date("Task without due date")
        self.assertIsNone(result)
    
    def test_parse_due_case_insensitive(self):
        """Test that due: prefix is case-insensitive."""
        result = parse_due_date("Task DUE:tomorrow")
        self.assertIsNotNone(result)


class TestExtractDescription(unittest.TestCase):
    """Test cases for description extraction."""
    
    def test_extract_with_tag(self):
        """Test extracting description with tag removed."""
        result = extract_description("Complete project #Projects")
        self.assertEqual(result, "Complete project")
    
    def test_extract_with_due_date(self):
        """Test extracting description with due date removed."""
        result = extract_description("Complete project due:tomorrow")
        self.assertEqual(result, "Complete project")
    
    def test_extract_with_both(self):
        """Test extracting description with both tag and due date removed."""
        result = extract_description("Complete project #Projects due:tomorrow")
        self.assertEqual(result, "Complete project")
    
    def test_extract_clean_whitespace(self):
        """Test that extra whitespace is cleaned up."""
        result = extract_description("Task  #Projects   due:tomorrow  extra")
        self.assertEqual(result, "Task extra")


class TestParseTask(unittest.TestCase):
    """Test cases for full task parsing."""
    
    def test_parse_complete_task(self):
        """Test parsing a complete task with tags and due date."""
        result = parse_task("Review quantum parables #Timeline #Quantum due:2025-12-01")
        
        self.assertIsInstance(result, ParsedTask)
        self.assertEqual(result.original_text, "Review quantum parables #Timeline #Quantum due:2025-12-01")
        self.assertEqual(result.description, "Review quantum parables")
        self.assertEqual(len(result.tags), 2)
        self.assertIn("#Timeline", result.tags)
        self.assertIn("#Quantum", result.tags)
        self.assertIsNotNone(result.due_date)
        self.assertEqual(result.due_date.year, 2025)
        self.assertEqual(result.due_date.month, 12)
        self.assertEqual(result.due_date.day, 1)
    
    def test_parse_minimal_task(self):
        """Test parsing a minimal task with no tags or due date."""
        result = parse_task("Simple task")
        
        self.assertEqual(result.description, "Simple task")
        self.assertEqual(result.tags, [])
        self.assertIsNone(result.due_date)


class TestDatabaseOperations(unittest.TestCase):
    """Test cases for database operations."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test database."""
        # Use a test database file
        import scrolls.task_parser as tp
        tp.DB_FILE = "/tmp/test_tasks.db"
        
        # Remove existing test database
        if os.path.exists(tp.DB_FILE):
            os.remove(tp.DB_FILE)
        
        init_database()
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test database."""
        import scrolls.task_parser as tp
        if os.path.exists(tp.DB_FILE):
            os.remove(tp.DB_FILE)
    
    def test_save_and_get_task(self):
        """Test saving and retrieving a task."""
        parsed = parse_task("Test task #Projects due:tomorrow")
        task_id = save_task(parsed)
        
        self.assertIsNotNone(task_id)
        self.assertGreater(task_id, 0)
        
        retrieved = get_task(task_id)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved['description'], "Test task")
        self.assertIn("#Projects", retrieved['tags'])
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        # Save a few tasks
        parse_and_save_task("Task 1 #Personal")
        parse_and_save_task("Task 2 #Timeline")
        
        tasks = get_all_tasks()
        self.assertGreater(len(tasks), 0)
    
    def test_get_tasks_by_tag(self):
        """Test filtering tasks by tag."""
        parse_and_save_task("Tagged task #Scripture")
        
        tasks = get_tasks_by_tag("#Scripture")
        self.assertGreater(len(tasks), 0)
        for task in tasks:
            self.assertIn("#Scripture", task['tags'])
    
    def test_mark_task_completed(self):
        """Test marking a task as completed."""
        parsed, task_id = parse_and_save_task("Complete me #Projects")
        
        success = mark_task_completed(task_id, True)
        self.assertTrue(success)
        
        task = get_task(task_id)
        self.assertEqual(task['completed'], 1)
    
    def test_delete_task(self):
        """Test deleting a task."""
        parsed, task_id = parse_and_save_task("Delete me #Projects")
        
        success = delete_task(task_id)
        self.assertTrue(success)
        
        task = get_task(task_id)
        self.assertIsNone(task)


if __name__ == '__main__':
    unittest.main()
