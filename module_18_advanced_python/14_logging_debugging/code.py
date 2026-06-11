# ============================================
# MODULE 18 - SUBTOPIC 14: Logging & Debugging
# ============================================

# Professional-grade logging and debugging techniques.

import logging
import sys
import os
import traceback

# =============================
# 1. BASIC LOGGING
# =============================

# Reset logging for this script
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s | %(message)s'
)

print("=== Basic Logging Levels ===")
print()

logging.debug("This is a DEBUG message — detailed diagnostic info")
logging.info("This is an INFO message — normal operation")
logging.warning("This is a WARNING — something unexpected")
logging.error("This is an ERROR — something failed")
logging.critical("This is CRITICAL — system may crash")
print()

# =============================
# 2. LOGGING WITH TIMESTAMPS
# =============================

# Reconfigure with timestamps
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S'
)

print("=== Logging with Timestamps ===")
print()

logging.info("Application started")
logging.debug("Loading configuration...")
logging.info("Configuration loaded successfully")
logging.warning("Using default settings for missing config key")
print()

# =============================
# 3. NAMED LOGGERS
# =============================

print("=== Named Loggers ===")
print()

# Each module/component gets its own logger
db_logger = logging.getLogger("database")
api_logger = logging.getLogger("api")
auth_logger = logging.getLogger("auth")

db_logger.info("Connected to database")
api_logger.info("API server started on port 8080")
auth_logger.warning("Failed login attempt from 192.168.1.100")
db_logger.error("Query timeout after 30s")
print()

# The logger name helps you identify WHERE a message came from

# =============================
# 4. LOGGING TO A FILE
# =============================

print("=== Logging to a File ===")
print()

script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "_demo_app.log")

# Create a file handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(
    logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
)

file_logger = logging.getLogger("file_demo")
file_logger.addHandler(file_handler)

file_logger.info("This goes to the log file")
file_logger.warning("This also goes to the log file")
file_logger.debug("This does NOT go to file (level too low)")

# Read back the log file
with open(log_file, "r") as f:
    print(f"  Log file contents:")
    for line in f:
        print(f"    {line.strip()}")
print()

# Clean up
file_handler.close()
os.remove(log_file)

# =============================
# 5. MULTIPLE HANDLERS
# =============================

print("=== Multiple Handlers ===")
print()

# A logger can send messages to MULTIPLE destinations
multi_logger = logging.getLogger("multi")
multi_logger.setLevel(logging.DEBUG)

# Console handler — show WARNING and above
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(
    logging.Formatter('  CONSOLE | %(levelname)s | %(message)s')
)

multi_logger.addHandler(console_handler)

multi_logger.debug("Debug — console won't show this")
multi_logger.info("Info — console won't show this")
multi_logger.warning("Warning — console WILL show this")
multi_logger.error("Error — console WILL show this")
print()

multi_logger.removeHandler(console_handler)

# =============================
# 6. STRUCTURED LOGGING WITH EXTRA DATA
# =============================

print("=== Structured Logging ===")
print()

struct_logger = logging.getLogger("structured")

# Log with extra context using f-strings
user_id = 12345
action = "login"
ip_address = "192.168.1.50"

struct_logger.info(f"User action: user_id={user_id} action={action} ip={ip_address}")

# Log with dictionary data
request_data = {"method": "POST", "path": "/api/users", "status": 201}
struct_logger.info(f"Request: {request_data}")
print()

# =============================
# 7. EXCEPTION LOGGING
# =============================

print("=== Exception Logging ===")
print()

exc_logger = logging.getLogger("exceptions")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        exc_logger.error("Division by zero!", exc_info=True)
        return None

result = divide(10, 0)
print(f"  Result: {result}")
print()

# exc_info=True adds the full traceback to the log
# This is much better than just logging the error message

# =============================
# 8. TRACEBACK MODULE FOR DEBUGGING
# =============================

print("=== Traceback Module ===")
print()

def function_a():
    return function_b()

def function_b():
    return function_c()

def function_c():
    raise RuntimeError("Something went wrong in function_c")

try:
    function_a()
except RuntimeError:
    # Get formatted traceback as a string
    tb = traceback.format_exc()
    print(f"  Caught traceback:\n{tb}")

# =============================
# 9. DEBUGGING WITH ASSERTIONS
# =============================

print("=== Assertions for Debugging ===")
print()

def calculate_average(scores):
    assert len(scores) > 0, "Scores list cannot be empty"
    assert all(isinstance(s, (int, float)) for s in scores), "All scores must be numbers"
    assert all(0 <= s <= 100 for s in scores), "Scores must be between 0 and 100"
    return sum(scores) / len(scores)

# Valid call
avg = calculate_average([85, 90, 78, 92])
print(f"  Average: {avg}")

# Invalid calls — assertions catch errors early
try:
    calculate_average([])
except AssertionError as e:
    print(f"  Assertion caught: {e}")

try:
    calculate_average([85, 110, 92])
except AssertionError as e:
    print(f"  Assertion caught: {e}")
print()

# =============================
# 10. PRACTICAL: APPLICATION LOGGER
# =============================

print("=== Practical: Application Logger ===")
print()

class AppLogger:
    """A simple application logger with context."""
    
    def __init__(self, app_name):
        self.logger = logging.getLogger(app_name)
        self.logger.setLevel(logging.DEBUG)
        
        # Add a clean console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter(f'  [{app_name}] %(levelname)s: %(message)s')
        )
        self.logger.addHandler(handler)
        self._handler = handler
    
    def info(self, msg):
        self.logger.info(msg)
    
    def warn(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg, exc_info=False):
        self.logger.error(msg, exc_info=exc_info)
    
    def cleanup(self):
        self.logger.removeHandler(self._handler)

# Usage
app = AppLogger("MyApp")
app.info("Starting application")
app.info("Loading user data")
app.warn("Cache miss — fetching from database")
app.info("Loaded 150 users")
app.error("Failed to connect to notification service")
app.info("Application ready")
app.cleanup()
print()

# =============================
# 11. DEBUGGING TIPS SUMMARY
# =============================

print("=== Debugging Tips ===")
print()

tips = [
    "Use logging instead of print() for production code",
    "Set appropriate log levels (DEBUG for dev, WARNING for prod)",
    "Include timestamps and context in log messages",
    "Use exc_info=True when logging exceptions",
    "Use assertions to catch bugs during development",
    "Use traceback.format_exc() to capture error details",
    "Use breakpoint() to start interactive debugging",
    "Name your loggers after modules/components",
]

for i, tip in enumerate(tips, 1):
    print(f"  {i}. {tip}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a logger that writes to both console and file
# 2. Log the execution of a multi-step process with
#    appropriate levels (INFO for steps, ERROR for failures)
# 3. Use traceback to capture and log exceptions in
#    a try/except block
# ============================================
