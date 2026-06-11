# Logging & Debugging

## Why Use Logging?

`print()` works for debugging, but it has limits:
- No severity levels (is it an error or info?)
- No timestamps
- Can't easily turn off in production
- Can't write to files

The `logging` module solves all of these.

## Logging Levels

| Level | Value | When to Use |
|-------|-------|------------|
| DEBUG | 10 | Detailed diagnostic information |
| INFO | 20 | Normal operation confirmations |
| WARNING | 30 | Something unexpected (default level) |
| ERROR | 40 | A function failed |
| CRITICAL | 50 | Program may crash |

```python
import logging

logging.debug("Detailed info")      # Not shown by default
logging.info("System started")      # Not shown by default
logging.warning("Low memory")       # Shown
logging.error("File not found")     # Shown
logging.critical("System crash!")   # Shown
```

## Basic Configuration

```python
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## Logging to a File

```python
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Debugging with pdb

```python
# Add this line where you want to pause:
breakpoint()

# Or use pdb directly:
import pdb; pdb.set_trace()
```

This drops you into an interactive debugger where you can inspect variables.

## Key Points

- Use `logging` instead of `print()` for anything beyond quick debugging
- Choose the right level: DEBUG < INFO < WARNING < ERROR < CRITICAL
- Configure format, level, and output destination with `basicConfig()`
- Use named loggers for different parts of your application
- `breakpoint()` starts the interactive debugger
