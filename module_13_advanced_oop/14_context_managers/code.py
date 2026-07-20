# ============================================
# MODULE 13 - SUBTOPIC 14: Context Managers
# ============================================

# Context managers use __enter__ and __exit__ for automatic
# setup and cleanup with the 'with' statement.

import time

# =============================
# 1. BASIC CONTEXT MANAGER
# =============================

# --- Example 1: Timer context manager ---
print("=== Basic Context Manager: Timer ===")
print()

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("    Timer started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"    Timer stopped: {self.elapsed:.4f}s")
        return False    # don't suppress exceptions

with Timer() as t:
    # Do some work
    total = sum(range(100000))
    print(f"    Sum computed: {total}")

print()

# =============================
# 2. HOW with WORKS
# =============================

# --- Example 2: Seeing __enter__ and __exit__ ---
print("=== How 'with' Works ===")
print()

class Managed:
    def __enter__(self):
        print("    1. __enter__ called (setup)")
        return self     # this becomes the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("    3. __exit__ called (cleanup)")
        return False

print("  Using 'with' statement:")
with Managed() as m:
    print("    2. Inside the 'with' block")

print("  4. After the 'with' block")
print()

# =============================
# 3. RESOURCE MANAGEMENT
# =============================

# --- Example 3: Database connection (simulated) ---
print("=== Resource Management ===")
print()

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        self.connected = True
        print(f"    Connected to '{self.db_name}'")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        print(f"    Disconnected from '{self.db_name}'")
        return False

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected!")
        return f"Results for: {sql}"

# Connection is automatically closed!
with DatabaseConnection("myapp.db") as db:
    result = db.query("SELECT * FROM users")
    print(f"    {result}")

# db is disconnected here
print(f"  Still connected? {db.connected}")
print()

# =============================
# 4. ERROR HANDLING IN __exit__
# =============================

# --- Example 4: __exit__ always runs, even on errors ---
print("=== Error Handling ===")
print()

class SafeFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print(f"    Opening '{self.filename}'")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"    Closing '{self.filename}'")
        if exc_type is not None:
            print(f"    Error occurred: {exc_type.__name__}: {exc_val}")
        return False    # False = propagate the exception

# Normal case
with SafeFile("data.txt") as f:
    print("    Reading data...")

print()

# Error case — __exit__ STILL runs
try:
    with SafeFile("broken.txt") as f:
        print("    Processing...")
        raise ValueError("Something went wrong!")
except ValueError:
    print("    Exception was propagated")
print()

# =============================
# 5. SUPPRESSING EXCEPTIONS
# =============================

# --- Example 5: Return True from __exit__ to suppress ---
print("=== Suppressing Exceptions ===")
print()

class ErrorSuppressor:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"    Suppressed: {exc_type.__name__}: {exc_val}")
        return True     # True = suppress the exception!

with ErrorSuppressor():
    print("    This runs")
    raise ValueError("This error is suppressed!")

print("    Code continues — error was suppressed!")
print()

# =============================
# 6. TEMPORARY STATE CHANGE
# =============================

# --- Example 6: Change and restore state ---
print("=== Temporary State ===")
print()

class TemporaryAttribute:
    def __init__(self, obj, attr, value):
        self.obj = obj
        self.attr = attr
        self.new_value = value

    def __enter__(self):
        self.old_value = getattr(self.obj, self.attr)
        setattr(self.obj, self.attr, self.new_value)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.obj, self.attr, self.old_value)
        return False

class AppConfig:
    def __init__(self):
        self.debug = False
        self.verbose = False

config = AppConfig()
print(f"  Before: debug={config.debug}")

with TemporaryAttribute(config, "debug", True):
    print(f"  Inside: debug={config.debug}")

print(f"  After:  debug={config.debug}")
print()

# =============================
# 7. PRACTICAL: INDENTED PRINTER
# =============================

# --- Example 7: Nested indentation manager ---
print("=== Indented Printer ===")
print()

class IndentedBlock:
    _level = 0

    def __init__(self, title=""):
        self.title = title

    def __enter__(self):
        if self.title:
            print("  " + "  " * IndentedBlock._level + self.title)
        IndentedBlock._level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        IndentedBlock._level -= 1
        return False

    @staticmethod
    def print(text):
        print("  " + "  " * IndentedBlock._level + text)

with IndentedBlock("Project:"):
    IndentedBlock.print("src/")
    with IndentedBlock("app/"):
        IndentedBlock.print("main.py")
        IndentedBlock.print("utils.py")
    with IndentedBlock("tests/"):
        IndentedBlock.print("test_main.py")
    IndentedBlock.print("README.md")

# ============================================
# TRY IT YOURSELF:
# 1. Create a Timer that prints elapsed time
# 2. Create a "WorkingDirectory" context manager (prints enter/exit)
# 3. Create a context manager that counts how many errors occur
# ============================================
