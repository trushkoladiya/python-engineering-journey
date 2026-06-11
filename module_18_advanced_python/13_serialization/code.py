# ============================================
# MODULE 18 - SUBTOPIC 13: Serialization & Data Handling
# ============================================

# Converting Python objects to/from storable formats.
# JSON for universal data, pickle for Python-specific objects.

import json
import pickle
import os
import tempfile

# =============================
# 1. JSON BASICS
# =============================

print("=== JSON Basics ===")
print()

# Python dict → JSON string
user = {
    "name": "Trush",
    "age": 21,
    "active": True,
    "scores": [95, 87, 92],
    "address": None
}

json_string = json.dumps(user)
print(f"  JSON string: {json_string}")
print(f"  Type: {type(json_string)}")
print()

# Pretty-printed JSON
pretty = json.dumps(user, indent=2)
print(f"  Pretty JSON:\n{pretty}")
print()

# =============================
# 2. JSON PARSING
# =============================

print("=== JSON Parsing ===")
print()

# JSON string → Python dict
json_text = '{"name": "Rahul", "age": 25, "languages": ["Python", "Go"]}'
parsed = json.loads(json_text)

print(f"  Parsed: {parsed}")
print(f"  Type: {type(parsed)}")
print(f"  Name: {parsed['name']}")
print(f"  Languages: {parsed['languages']}")
print()

# =============================
# 3. JSON TYPE MAPPING
# =============================

print("=== JSON Type Mapping ===")
print()

data = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "null_value": None,
    "list": [1, 2, 3],
    "nested": {"a": 1, "b": 2}
}

json_out = json.dumps(data, indent=2)
print(f"  Python → JSON:\n{json_out}")
print()

# Note: JSON keys must be strings
# Tuples become arrays, sets are NOT supported directly

# =============================
# 4. JSON FILE I/O
# =============================

print("=== JSON File I/O ===")
print()

# Create a temporary file for demo
script_dir = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(script_dir, "_demo_data.json")

# Write JSON to file
config = {
    "app_name": "MyApp",
    "version": "2.0",
    "debug": False,
    "max_users": 100,
    "features": ["login", "dashboard", "reports"]
}

with open(json_file, "w") as f:
    json.dump(config, f, indent=2)
print(f"  Wrote config to {os.path.basename(json_file)}")

# Read JSON from file
with open(json_file, "r") as f:
    loaded_config = json.load(f)
print(f"  Loaded: {loaded_config}")
print(f"  App name: {loaded_config['app_name']}")
print()

# Clean up
os.remove(json_file)

# =============================
# 5. HANDLING SPECIAL TYPES IN JSON
# =============================

print("=== Handling Special Types ===")
print()

# Sets, tuples, and custom objects need conversion
from datetime import datetime, date

# Custom encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

special_data = {
    "timestamp": datetime(2025, 1, 15, 10, 30),
    "tags": {"python", "coding", "tutorial"},
    "count": 42
}

encoded = json.dumps(special_data, cls=CustomEncoder, indent=2)
print(f"  Custom encoded:\n{encoded}")
print()

# =============================
# 6. JSON WITH SORTING AND SEPARATORS
# =============================

print("=== JSON Formatting Options ===")
print()

data = {"banana": 2, "apple": 5, "cherry": 1}

# Sort keys alphabetically
sorted_json = json.dumps(data, sort_keys=True, indent=2)
print(f"  Sorted keys:\n{sorted_json}")

# Compact output (minimal whitespace)
compact = json.dumps(data, separators=(',', ':'))
print(f"  Compact: {compact}")

# With extra spacing
spaced = json.dumps(data, separators=(', ', ': '))
print(f"  Spaced: {spaced}")
print()

# =============================
# 7. PICKLE BASICS
# =============================

print("=== Pickle Basics ===")
print()

# Pickle can serialize almost ANY Python object
data = {
    "name": "Trush",
    "scores": [95, 87, 92],
    "metadata": {"grade": "A", "passed": True}
}

# Serialize to bytes
pickled = pickle.dumps(data)
print(f"  Pickled type: {type(pickled)}")
print(f"  Pickled size: {len(pickled)} bytes")

# Deserialize back
restored = pickle.loads(pickled)
print(f"  Restored: {restored}")
print(f"  Equal: {data == restored}")
print()

# =============================
# 8. PICKLE WITH CUSTOM OBJECTS
# =============================

print("=== Pickle: Custom Objects ===")
print()

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        self.average = sum(grades) / len(grades)
    
    def __repr__(self):
        return f"Student({self.name}, avg={self.average:.1f})"

students = [
    Student("Trush", [95, 87, 92]),
    Student("Rahul", [88, 76, 91]),
    Student("Charlie", [92, 95, 89]),
]

# Pickle custom objects
pickled_students = pickle.dumps(students)
restored_students = pickle.loads(pickled_students)

print(f"  Original: {students}")
print(f"  Restored: {restored_students}")
print()

# JSON can't handle custom objects without extra work
# Pickle handles them natively

# =============================
# 9. PICKLE FILE I/O
# =============================

print("=== Pickle File I/O ===")
print()

pickle_file = os.path.join(script_dir, "_demo_data.pkl")

# Write to file
with open(pickle_file, "wb") as f:  # Note: "wb" for binary
    pickle.dump(students, f)
print(f"  Saved {len(students)} students to pickle file")

# Read from file
with open(pickle_file, "rb") as f:  # Note: "rb" for binary
    loaded = pickle.load(f)
print(f"  Loaded: {loaded}")
print()

os.remove(pickle_file)

# =============================
# 10. JSON vs PICKLE COMPARISON
# =============================

print("=== JSON vs Pickle ===")
print()

test_data = {
    "users": [
        {"name": "Trush", "age": 21, "active": True},
        {"name": "Rahul", "age": 25, "active": False},
    ],
    "count": 2,
    "version": "1.0"
}

json_bytes = json.dumps(test_data).encode()
pickle_bytes = pickle.dumps(test_data)

print(f"  JSON size:   {len(json_bytes)} bytes (human readable)")
print(f"  Pickle size: {len(pickle_bytes)} bytes (binary)")
print()

print("  ┌──────────────┬───────────────┬───────────────┐")
print("  │ Feature      │ JSON          │ Pickle        │")
print("  ├──────────────┼───────────────┼───────────────┤")
print("  │ Readable     │ ✅ Yes         │ ❌ No          │")
print("  │ Cross-lang   │ ✅ Yes         │ ❌ Python only  │")
print("  │ Security     │ ✅ Safe        │ ⚠️  Dangerous  │")
print("  │ All types    │ ❌ Limited     │ ✅ Everything   │")
print("  │ Speed        │ Moderate      │ Fast          │")
print("  └──────────────┴───────────────┴───────────────┘")
print()

# =============================
# 11. PRACTICAL: CONFIG FILE MANAGER
# =============================

print("=== Practical: Config Manager ===")
print()

class ConfigManager:
    """Manage application configuration with JSON."""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.config = {}
    
    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self.config = json.load(f)
        return self
    
    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.config, f, indent=2)
        return self
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        return self
    
    def __repr__(self):
        return f"Config({self.config})"

config_file = os.path.join(script_dir, "_app_config.json")

mgr = ConfigManager(config_file)
mgr.set("theme", "dark")
mgr.set("language", "en")
mgr.set("font_size", 14)
mgr.save()

print(f"  Saved: {mgr}")

# Load in a new instance
mgr2 = ConfigManager(config_file).load()
print(f"  Loaded: {mgr2}")
print(f"  Theme: {mgr2.get('theme')}")
print()

os.remove(config_file)

# ============================================
# TRY IT YOURSELF:
# 1. Create a JSON file with a list of books
#    (title, author, year) and read it back
# 2. Use pickle to save and load a complex nested
#    data structure with custom objects
# 3. Build a simple "database" that stores records
#    in a JSON file with add/search/delete operations
# ============================================
