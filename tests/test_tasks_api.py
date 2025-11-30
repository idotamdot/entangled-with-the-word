"""Tests for the task history API endpoint."""
import pytest
from fastapi.testclient import TestClient

from api.main import app
from api import models


@pytest.fixture(autouse=True)
def use_temp_tasks_file(monkeypatch, tmp_path):
    """Use a temporary file for tasks during tests."""
    temp_file = tmp_path / "tasks.csv"
    monkeypatch.setattr(models, "TASKS_FILE", str(temp_file))
    yield temp_file


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


class TestGetTasks:
    """Tests for GET /tasks endpoint."""

    def test_get_tasks_empty(self, client):
        """Test getting tasks when no tasks exist."""
        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.json() == []

    def test_get_tasks_with_data(self, client, use_temp_tasks_file):
        """Test getting tasks when tasks exist."""
        # Create some test tasks
        models.create_task(title="Test Task 1", tag="#Projects")
        models.create_task(title="Test Task 2", tag="#Personal")

        response = client.get("/tasks")
        assert response.status_code == 200
        tasks = response.json()
        assert len(tasks) == 2
        assert tasks[0]["title"] == "Test Task 1"
        assert tasks[1]["title"] == "Test Task 2"

    def test_get_tasks_filter_by_tag(self, client, use_temp_tasks_file):
        """Test filtering tasks by tag."""
        models.create_task(title="Project Task", tag="#Projects")
        models.create_task(title="Personal Task", tag="#Personal")

        response = client.get("/tasks?tag=%23Projects")
        assert response.status_code == 200
        tasks = response.json()
        assert len(tasks) == 1
        assert tasks[0]["title"] == "Project Task"

    def test_get_tasks_filter_by_status(self, client, use_temp_tasks_file):
        """Test filtering tasks by status."""
        models.create_task(title="Pending Task")
        task2 = models.create_task(title="Completed Task")
        # Manually update status for testing
        df = models.load_tasks()
        df.loc[df["id"] == task2["id"], "status"] = "completed"
        models.save_tasks(df)

        response = client.get("/tasks?status=pending")
        assert response.status_code == 200
        tasks = response.json()
        assert len(tasks) == 1
        assert tasks[0]["title"] == "Pending Task"


class TestRootEndpoint:
    """Tests for root endpoint."""

    def test_root(self, client):
        """Test root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
