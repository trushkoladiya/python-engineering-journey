# ============================================
# MODULE 18 - SUBTOPIC 20: Engineering-Level Thinking
# ============================================

# Building systems, not scripts.
# Thinking like a software engineer.

import os
import json
import logging
import time
from datetime import datetime
from collections import defaultdict

# =============================
# 1. SYSTEM DESIGN: TASK MANAGER
# =============================

# Let's build a small but REAL system with:
# - Clean architecture (separated concerns)
# - Error handling
# - Logging
# - Data persistence
# - Testable design

print("=" * 60)
print("  ENGINEERING DEMO: Task Management System")
print("=" * 60)
print()

# =============================
# 2. CONFIGURATION
# =============================

# Good engineering: configuration is separate from logic

class Config:
    """Application configuration — single source of truth."""
    
    APP_NAME = "TaskManager"
    VERSION = "1.0.0"
    MAX_TITLE_LENGTH = 100
    VALID_PRIORITIES = ("low", "medium", "high", "critical")
    VALID_STATUSES = ("todo", "in_progress", "done", "cancelled")
    DEFAULT_PRIORITY = "medium"
    DEFAULT_STATUS = "todo"

# =============================
# 3. CUSTOM EXCEPTIONS
# =============================

# Good engineering: specific exceptions for specific errors

class TaskError(Exception):
    """Base exception for Task system."""
    pass

class ValidationError(TaskError):
    """Raised when input validation fails."""
    pass

class TaskNotFoundError(TaskError):
    """Raised when a task is not found."""
    pass

class DuplicateTaskError(TaskError):
    """Raised when a duplicate task is detected."""
    pass

# =============================
# 4. DATA MODEL
# =============================

# Good engineering: clear data model with validation

class Task:
    """Represents a single task."""
    
    _next_id = 1  # Auto-incrementing ID
    
    def __init__(self, title, description="", priority=None, status=None):
        self.id = Task._next_id
        Task._next_id += 1
        
        self.title = self._validate_title(title)
        self.description = description
        self.priority = self._validate_priority(priority or Config.DEFAULT_PRIORITY)
        self.status = self._validate_status(status or Config.DEFAULT_STATUS)
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    @staticmethod
    def _validate_title(title):
        if not title or not title.strip():
            raise ValidationError("Title cannot be empty")
        if len(title) > Config.MAX_TITLE_LENGTH:
            raise ValidationError(f"Title exceeds {Config.MAX_TITLE_LENGTH} characters")
        return title.strip()
    
    @staticmethod
    def _validate_priority(priority):
        if priority not in Config.VALID_PRIORITIES:
            raise ValidationError(
                f"Invalid priority '{priority}'. "
                f"Must be one of: {Config.VALID_PRIORITIES}"
            )
        return priority
    
    @staticmethod
    def _validate_status(status):
        if status not in Config.VALID_STATUSES:
            raise ValidationError(
                f"Invalid status '{status}'. "
                f"Must be one of: {Config.VALID_STATUSES}"
            )
        return status
    
    def update_status(self, new_status):
        """Update task status with validation."""
        self.status = self._validate_status(new_status)
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Serialize task to dictionary (for JSON storage)."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
    
    def __repr__(self):
        return f"Task({self.id}, '{self.title}', {self.status}, {self.priority})"

# =============================
# 5. SERVICE LAYER (Business Logic)
# =============================

# Good engineering: business logic is in a service layer,
# separate from data and presentation

class TaskService:
    """Business logic for managing tasks."""
    
    def __init__(self):
        self._tasks = {}  # id -> Task
        self._logger = logging.getLogger("TaskService")
    
    def create_task(self, title, description="", priority=None):
        """Create a new task."""
        task = Task(title, description, priority)
        self._tasks[task.id] = task
        self._logger.info(f"Created task #{task.id}: '{task.title}'")
        return task
    
    def get_task(self, task_id):
        """Get a task by ID."""
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task #{task_id} not found")
        return self._tasks[task_id]
    
    def update_status(self, task_id, new_status):
        """Update a task's status."""
        task = self.get_task(task_id)
        old_status = task.status
        task.update_status(new_status)
        self._logger.info(
            f"Task #{task_id} status: {old_status} → {new_status}"
        )
        return task
    
    def delete_task(self, task_id):
        """Delete a task."""
        task = self.get_task(task_id)
        del self._tasks[task_id]
        self._logger.info(f"Deleted task #{task_id}: '{task.title}'")
        return task
    
    def get_all_tasks(self, status=None, priority=None):
        """Get all tasks, optionally filtered."""
        tasks = list(self._tasks.values())
        
        if status:
            tasks = [t for t in tasks if t.status == status]
        if priority:
            tasks = [t for t in tasks if t.priority == priority]
        
        return tasks
    
    def get_statistics(self):
        """Get task statistics."""
        tasks = list(self._tasks.values())
        
        if not tasks:
            return {"total": 0}
        
        stats = {
            "total": len(tasks),
            "by_status": defaultdict(int),
            "by_priority": defaultdict(int),
        }
        
        for task in tasks:
            stats["by_status"][task.status] += 1
            stats["by_priority"][task.priority] += 1
        
        stats["by_status"] = dict(stats["by_status"])
        stats["by_priority"] = dict(stats["by_priority"])
        
        return stats

# =============================
# 6. PRESENTATION LAYER
# =============================

# Good engineering: presentation is separate from logic

class TaskPresenter:
    """Format tasks for display."""
    
    PRIORITY_SYMBOLS = {
        "low": "○",
        "medium": "●",
        "high": "▲",
        "critical": "🔴",
    }
    
    STATUS_SYMBOLS = {
        "todo": "☐",
        "in_progress": "◐",
        "done": "☑",
        "cancelled": "☒",
    }
    
    @classmethod
    def format_task(cls, task):
        """Format a single task for display."""
        p = cls.PRIORITY_SYMBOLS.get(task.priority, "?")
        s = cls.STATUS_SYMBOLS.get(task.status, "?")
        return f"  {s} #{task.id:3d} [{p} {task.priority:8s}] {task.title}"
    
    @classmethod
    def format_task_list(cls, tasks, title="Tasks"):
        """Format a list of tasks."""
        lines = [f"  === {title} ({len(tasks)}) ==="]
        if not tasks:
            lines.append("  (no tasks)")
        for task in tasks:
            lines.append(cls.format_task(task))
        return "\n".join(lines)
    
    @classmethod
    def format_statistics(cls, stats):
        """Format statistics for display."""
        lines = [f"  === Statistics ==="]
        lines.append(f"  Total tasks: {stats['total']}")
        
        if stats.get("by_status"):
            lines.append("  By status:")
            for status, count in sorted(stats["by_status"].items()):
                bar = "█" * count
                lines.append(f"    {status:12s}: {count:3d} {bar}")
        
        if stats.get("by_priority"):
            lines.append("  By priority:")
            for priority, count in sorted(stats["by_priority"].items()):
                bar = "█" * count
                lines.append(f"    {priority:12s}: {count:3d} {bar}")
        
        return "\n".join(lines)

# =============================
# 7. PUTTING IT ALL TOGETHER
# =============================

# Set up logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(
    level=logging.INFO,
    format='  LOG | %(name)s | %(message)s'
)

print()
print("--- Creating Tasks ---")
print()

service = TaskService()

# Create tasks
tasks_data = [
    ("Set up project structure", "Create directories and files", "high"),
    ("Write user authentication", "Login and registration", "critical"),
    ("Design database schema", "Plan tables and relationships", "high"),
    ("Create API endpoints", "REST API for frontend", "medium"),
    ("Write unit tests", "Cover core functionality", "medium"),
    ("Add logging", "Structured logging throughout", "low"),
    ("Deploy to staging", "Test in staging environment", "medium"),
    ("Write documentation", "API docs and README", "low"),
]

for title, desc, priority in tasks_data:
    service.create_task(title, desc, priority)

print()
print("--- All Tasks ---")
print()

all_tasks = service.get_all_tasks()
print(TaskPresenter.format_task_list(all_tasks))
print()

# =============================
# 8. UPDATE AND FILTER
# =============================

print("--- Updating Tasks ---")
print()

service.update_status(1, "done")
service.update_status(2, "in_progress")
service.update_status(3, "done")
service.update_status(6, "done")

print()
print("--- High Priority Tasks ---")
print()

high_priority = service.get_all_tasks(priority="high")
print(TaskPresenter.format_task_list(high_priority, "High Priority"))
print()

print("--- In Progress ---")
print()

in_progress = service.get_all_tasks(status="in_progress")
print(TaskPresenter.format_task_list(in_progress, "In Progress"))
print()

# =============================
# 9. STATISTICS
# =============================

print("--- Statistics ---")
print()

stats = service.get_statistics()
print(TaskPresenter.format_statistics(stats))
print()

# =============================
# 10. ERROR HANDLING IN ACTION
# =============================

print("--- Error Handling ---")
print()

# Try to get a non-existent task
try:
    service.get_task(999)
except TaskNotFoundError as e:
    print(f"  Handled: {e}")

# Try to create a task with invalid priority
try:
    service.create_task("Bad task", priority="urgent")
except ValidationError as e:
    print(f"  Handled: {e}")

# Try to create a task with empty title
try:
    service.create_task("")
except ValidationError as e:
    print(f"  Handled: {e}")

print()

# =============================
# 11. ENGINEERING PRINCIPLES USED
# =============================

print("=" * 60)
print("  ENGINEERING PRINCIPLES IN THIS SYSTEM")
print("=" * 60)
print()

principles = [
    ("Separation of Concerns",
     "Config, Model, Service, Presenter — each has one job"),
    ("Data Validation",
     "All input is validated at the model level"),
    ("Custom Exceptions",
     "Specific errors for specific situations"),
    ("Logging",
     "Every important action is logged"),
    ("Clean Interfaces",
     "Service provides clean methods, hides internals"),
    ("Serialization",
     "to_dict() enables JSON persistence"),
    ("Configurability",
     "Settings in Config class, not hardcoded"),
    ("Testability",
     "Each component can be tested independently"),
    ("Presentation Separation",
     "Display logic separate from business logic"),
    ("Error Handling",
     "Graceful handling with meaningful messages"),
]

for i, (principle, description) in enumerate(principles, 1):
    print(f"  {i:2d}. {principle}")
    print(f"      → {description}")
    print()

# =============================
# 12. YOUR ENGINEERING JOURNEY
# =============================

print("=" * 60)
print("  🎓 CONGRATULATIONS!")
print("=" * 60)
print()
print("  You have completed ALL 18 MODULES of Python learning.")
print()
print("  You now understand:")
print("    ✓ Python basics, data types, and control flow")
print("    ✓ Functions, recursion, and scope")
print("    ✓ Object-Oriented Programming (basic + advanced)")
print("    ✓ File handling and error management")
print("    ✓ Iterators, generators, and functional programming")
print("    ✓ Data structures and algorithms")
print("    ✓ Concurrency (threads, processes, async)")
print("    ✓ Performance optimization and caching")
print("    ✓ Testing, logging, and debugging")
print("    ✓ Security, system interaction, and clean code")
print("    ✓ Engineering-level thinking and system design")
print()
print("  You went from ZERO to ENGINEERING LEVEL. 🚀")
print()
print("  Next steps:")
print("    1. Build real projects (web apps, APIs, tools)")
print("    2. Contribute to open source")
print("    3. Learn a web framework (Django, FastAPI, Flask)")
print("    4. Study databases (PostgreSQL, MongoDB)")
print("    5. Never stop learning!")
print()

# ============================================
# FINAL CHALLENGES:
# 1. Extend this Task Manager with file persistence
#    (save/load tasks from a JSON file)
# 2. Add a command-line interface using input()
# 3. Add unit tests for every Service method
# 4. Build your OWN project using these principles!
# ============================================
