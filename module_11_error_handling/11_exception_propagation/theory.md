# Exception Propagation

When an exception is raised, it **travels up** through the call chain until something catches it. This is called **propagation** (or "bubbling up").

## How Propagation Works

```python
def step_3():
    return int("hello")    # ValueError raised here!

def step_2():
    return step_3()        # Error passes through here

def step_1():
    return step_2()        # Error passes through here

step_1()                   # Program crashes here (uncaught)
```

The ValueError travels: `step_3` → `step_2` → `step_1` → crash!

## Catching at Different Levels

You can catch the exception at **any level** in the chain:

```python
def step_3():
    return int("hello")    # ValueError raised

def step_2():
    return step_3()        # Passes through

def step_1():
    try:
        return step_2()    # Caught here!
    except ValueError:
        print("Handled the error")
```

## The Traceback

When an exception goes uncaught, Python prints a **traceback** — it shows the full chain of function calls:

```
Traceback (most recent call last):
  File "script.py", line 10, in <module>
    step_1()
  File "script.py", line 7, in step_1
    return step_2()
  File "script.py", line 4, in step_2
    return step_3()
  File "script.py", line 1, in step_3
    return int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
```

Read it **bottom to top** — the bottom shows where the error happened, the top shows where it was called from.

## Key Points

- Exceptions **bubble up** through function calls
- They stop at the **first matching `except`** they find
- If nothing catches them, the program **crashes** with a traceback
- You can catch at **any level** — choose the level that makes sense
- Read tracebacks **bottom to top**
