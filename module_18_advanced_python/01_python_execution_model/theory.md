# Python Execution Model

## How Does Python Run Your Code?

When you run a `.py` file, Python doesn't execute your code directly. It goes through steps:

1. **Source code** (`.py`) → Python reads your text file
2. **Bytecode** (`.pyc`) → Python compiles it to a lower-level format
3. **PVM (Python Virtual Machine)** → PVM executes the bytecode

```
your_script.py  →  bytecode (.pyc)  →  PVM executes it
```

## What Is Bytecode?

Bytecode is an **intermediate representation** of your code — not human-readable, but not machine code either. Python stores it in `__pycache__/` folders as `.pyc` files.

```python
# You can see bytecode using the dis module
import dis

def greet(name):
    return f"Hello, {name}"

dis.dis(greet)
# Shows low-level instructions like LOAD_FAST, RETURN_VALUE
```

You never need to write bytecode — Python handles it automatically.

## What Is the PVM?

The **Python Virtual Machine** is a loop that reads bytecode instructions one by one and executes them. It's the "engine" inside Python.

- It's **not** a separate program you install
- It's **part of** the Python interpreter (`python3`)
- Every time you run `python3 script.py`, the PVM is working

## Interpreted vs Compiled

| Language | Type | What Happens |
|----------|------|-------------|
| C / Rust | Compiled | Source → Machine code → CPU runs it |
| Python | Interpreted | Source → Bytecode → PVM runs it |
| Java | Both | Source → Bytecode → JVM runs it |

Python is called **interpreted** because:
- No separate compilation step is needed
- Bytecode compilation happens automatically at runtime
- The PVM interprets bytecode, not the CPU directly

## Why Does This Matter?

- Python is **slower** than compiled languages (PVM adds overhead)
- But Python is **faster to write** and **easier to read**
- Understanding this helps you know **why** optimization matters (Module 18 topic 8)
- `.pyc` files speed up startup — Python skips re-compiling unchanged files

## Key Points

- Python compiles source to bytecode, then the PVM executes it
- Bytecode is stored in `__pycache__/` as `.pyc` files
- The PVM is the engine inside the Python interpreter
- This is why Python is called an "interpreted" language
