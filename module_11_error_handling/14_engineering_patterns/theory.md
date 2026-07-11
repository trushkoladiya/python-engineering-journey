# Engineering-Level Patterns

This subtopic covers **real-world strategies** that professional developers use to write robust, fail-safe programs.

## Fail-Safe Design

A fail-safe program **never crashes unexpectedly**. It handles every error gracefully.

### Pattern: Default Values on Failure

```python
def get_setting(config, key, default):
    try:
        return config[key]
    except KeyError:
        return default
```

### Pattern: Retry on Failure

```python
def fetch_with_retry(operation, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            return operation()
        except Exception as e:
            if attempt == max_attempts:
                raise
            print(f"Attempt {attempt} failed, retrying...")
```

## Graceful Degradation

When part of the system fails, the **rest keeps working**:

```python
def load_all_data(filenames):
    results = {}
    for filename in filenames:
        try:
            with open(filename) as f:
                results[filename] = f.read()
        except FileNotFoundError:
            results[filename] = None   # Skip, don't crash
    return results
```

## Input Validation Strategy

Validate **before** processing — catch problems early:

```python
def process_order(quantity, price):
    # Validate FIRST
    if not isinstance(quantity, int) or quantity < 1:
        raise ValueError("Quantity must be a positive integer")
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Price must be a positive number")

    # Process AFTER validation passes
    return quantity * price
```

### LBYL vs EAFP

| Style | Meaning | Approach |
|-------|---------|----------|
| **LBYL** | Look Before You Leap | Check conditions first, then act |
| **EAFP** | Easier to Ask Forgiveness | Try it, handle errors if they occur |

```python
# LBYL — check first
if key in data:
    value = data[key]

# EAFP — try and catch (Pythonic!)
try:
    value = data[key]
except KeyError:
    value = default
```

Python generally prefers **EAFP**.

## Key Points

- Design programs that **degrade gracefully** — don't crash on partial failures
- Use **default values** when operations might fail
- **Validate inputs early** to catch problems before they cause damage
- Prefer **EAFP** (try/except) over **LBYL** (if/check) in Python
- Build **retry logic** for operations that might transiently fail
