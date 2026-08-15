# Serialization & Data Handling

## What Is Serialization?

**Serialization** is converting a Python object into a format that can be **stored** (in a file) or **transmitted** (over a network), and later **reconstructed** back into a Python object.

```
Python Object → serialize → bytes/string → deserialize → Python Object
```

## JSON — The Universal Format

**JSON** (JavaScript Object Notation) is a text-based format that's human-readable and widely supported.

```python
import json

# Python → JSON string
data = {"name": "Trush", "age": 21, "scores": [95, 87, 92]}
json_string = json.dumps(data, indent=2)

# JSON string → Python
restored = json.loads(json_string)
```

### JSON Type Mapping

| Python | JSON |
|--------|------|
| dict | object |
| list | array |
| str | string |
| int/float | number |
| True/False | true/false |
| None | null |

## Pickle — Python-Specific Format

**Pickle** can serialize **any** Python object (even classes and functions), but:
- It's **Python-only** — other languages can't read it
- It's **not human-readable** — binary format
- **Never unpickle untrusted data** — it can execute arbitrary code

```python
import pickle

data = {"name": "Trush", "scores": [95, 87]}
pickled = pickle.dumps(data)       # Serialize
restored = pickle.loads(pickled)   # Deserialize
```

## JSON vs Pickle

| Feature | JSON | Pickle |
|---------|------|--------|
| Human readable | ✅ Yes | ❌ No |
| Cross-language | ✅ Yes | ❌ Python only |
| Security | ✅ Safe | ⚠️ Dangerous with untrusted data |
| All Python types | ❌ Limited | ✅ Everything |

## Key Points

- Use **JSON** for data exchange, APIs, config files (safe, universal)
- Use **pickle** only for Python-to-Python data and trusted sources
- `json.dumps()` / `json.loads()` for strings
- `json.dump()` / `json.load()` for files
- Never unpickle data from untrusted sources
