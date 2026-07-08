# Common Patterns (Engineering Thinking)

Real-world file handling patterns you'll use in actual projects.

## Log File Writing

```python
import datetime

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")
```

## Configuration File Reading

```python
def load_config(filepath):
    config = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config
```

## Simple Data Persistence

Save and load data between program runs:

```python
import json

# Save
with open("data.json", "w") as f:
    json.dump({"scores": [85, 92, 78]}, f)

# Load
with open("data.json", "r") as f:
    data = json.load(f)
```

## Key Points

- Log files use append mode — never overwrite logs
- Config files use key=value pairs, skip comments (#)
- JSON is great for saving structured data
- These patterns appear in nearly every real application
