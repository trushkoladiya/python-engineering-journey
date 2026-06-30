# Common Patterns (Engineering Thinking)

These patterns show how functions are used in real-world programming.

## Utility / Helper Functions

Small functions that do a single, common task:

```python
def clamp(value, min_val, max_val):
    """Keep value within min and max bounds."""
    if value < min_val: return min_val
    if value > max_val: return max_val
    return value
```

## Validation Functions

Check if data meets requirements:

```python
def is_valid_age(age):
    return isinstance(age, int) and 0 <= age <= 150
```

## Function Pipelines

Apply multiple functions in sequence:

```python
def clean(text):
    return text.strip()

def lowercase(text):
    return text.lower()

def remove_extra_spaces(text):
    return " ".join(text.split())

# Pipeline
data = "  Hello   World  "
data = clean(data)
data = lowercase(data)
data = remove_extra_spaces(data)
print(data)   # "hello world"
```

## Callback Pattern

Pass a function to control behavior:

```python
def process_items(items, action):
    for item in items:
        action(item)
```

## Key Points

- Utility functions handle common operations
- Validation functions keep data clean
- Pipelines chain functions for data transformation
- Callbacks let you customize behavior by passing functions
