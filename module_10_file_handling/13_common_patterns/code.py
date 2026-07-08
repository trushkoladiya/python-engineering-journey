# ============================================
# MODULE 10 - SUBTOPIC 13: Common Patterns
# ============================================

import os
import json
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. LOG FILE PATTERN
# =============================

log_file = os.path.join(SCRIPT_DIR, "app.log")

def log(message, level="INFO"):
    """Append a timestamped message to the log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] [{level}] {message}\n")

# --- Example 1: Writing log entries ---
log("Application started")
log("Loading configuration")
log("Processing 50 records")
log("Invalid input detected", "WARNING")
log("Processing complete")

print("Log file:")
with open(log_file, "r") as f:
    print(f.read(), end="")

# =============================
# 2. CONFIGURATION FILE PATTERN
# =============================

config_file = os.path.join(SCRIPT_DIR, "app.config")

# --- Example 2: Create a config file ---
with open(config_file, "w") as f:
    f.write("# Application Configuration\n")
    f.write("# Lines starting with # are comments\n\n")
    f.write("app_name = MyApp\n")
    f.write("version = 2.5\n")
    f.write("debug = true\n")
    f.write("max_users = 100\n")
    f.write("database = sqlite\n")

# --- Example 3: Read config file ---
def load_config(filepath):
    """Parse a key=value config file."""
    config = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config

config = load_config(config_file)
print("\nConfiguration:")
for key, value in config.items():
    print(f"  {key}: {value}")

# --- Example 4: Use config values ---
print(f"\nApp: {config.get('app_name', 'Unknown')}")
print(f"Debug: {config.get('debug', 'false')}")

# =============================
# 3. JSON DATA PERSISTENCE
# =============================

json_file = os.path.join(SCRIPT_DIR, "data.json")

# --- Example 5: Save data as JSON ---
data = {
    "users": [
        {"name": "Trush", "score": 95, "active": True},
        {"name": "Rahul", "score": 82, "active": True},
        {"name": "Charlie", "score": 78, "active": False},
    ],
    "metadata": {
        "total": 3,
        "version": "1.0",
    }
}

with open(json_file, "w") as f:
    json.dump(data, f, indent=2)

print(f"\nSaved JSON:")
with open(json_file, "r") as f:
    print(f.read())

# --- Example 6: Load JSON data ---
with open(json_file, "r") as f:
    loaded = json.load(f)

print("Loaded data:")
for user in loaded["users"]:
    status = "active" if user["active"] else "inactive"
    print(f"  {user['name']}: {user['score']} ({status})")

# =============================
# 4. SIMPLE DATABASE PATTERN
# =============================

db_file = os.path.join(SCRIPT_DIR, "simple_db.json")

# --- Example 7: CRUD operations with JSON file ---
def db_load(filepath):
    """Load database from file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as f:
        return json.load(f)

def db_save(filepath, data):
    """Save database to file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def db_add(filepath, key, value):
    """Add an entry to the database."""
    data = db_load(filepath)
    data[key] = value
    db_save(filepath, data)

def db_get(filepath, key, default=None):
    """Get an entry from the database."""
    data = db_load(filepath)
    return data.get(key, default)

# Using the simple database
print("\nSimple DB:")
db_add(db_file, "trush", {"age": 21, "email": "trushkoladiya.work@gmail.com"})
db_add(db_file, "rahul", {"age": 30, "email": "rahul@example.com"})

print(f"  trush: {db_get(db_file, 'trush')}")
print(f"  rahul: {db_get(db_file, 'rahul')}")
print(f"  unknown: {db_get(db_file, 'unknown', 'Not found')}")

# =============================
# 5. WORD COUNTER PATTERN
# =============================

text_file = os.path.join(SCRIPT_DIR, "article.txt")

# --- Example 8: Count words in a file ---
with open(text_file, "w") as f:
    f.write("Python is a great programming language.\n")
    f.write("Python is used for web development and data science.\n")
    f.write("Learning Python is fun and Python is powerful.\n")

def count_words(filepath):
    """Count word frequency in a file."""
    freq = {}
    with open(filepath, "r") as file:
        for line in file:
            for word in line.strip().lower().split():
                word = word.strip(".,!?;:")
                freq[word] = freq.get(word, 0) + 1
    return freq

word_freq = count_words(text_file)
print(f"\nWord frequency (top 8):")
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:8]:
    bar = "█" * count
    print(f"  {word:12s} {bar} ({count})")

# =============================
# 6. SEARCH IN FILES PATTERN
# =============================

# --- Example 9: Search for text in a file ---
def search_file(filepath, query):
    """Find lines containing the query."""
    results = []
    with open(filepath, "r") as file:
        for num, line in enumerate(file, 1):
            if query.lower() in line.lower():
                results.append((num, line.strip()))
    return results

print(f"\nSearch for 'python':")
matches = search_file(text_file, "python")
for line_num, line_text in matches:
    print(f"  Line {line_num}: {line_text}")

# =============================
# CLEANUP
# =============================
for f in ["app.log", "app.config", "data.json",
          "simple_db.json", "article.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print(f"\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Build a simple to-do list that saves to a file
# 2. Create a config reader that supports default values
# 3. Build a search tool that finds text across multiple files
# ============================================
