# Function Calling

Defining a function creates it. **Calling** a function runs it.

## Calling Functions

Use the function name followed by parentheses `()`:

```python
def greet():
    print("Hello!")

greet()   # This runs the function
```

## Execution Flow

When Python encounters a function **definition**, it skips the body. When it encounters a function **call**, it jumps into the body, runs it, and then comes back:

```python
print("Step 1")

def my_function():
    print("Step 2 — inside function")

print("Step 3")
my_function()    # NOW it runs
print("Step 4")
```

Output:
```
Step 1
Step 3
Step 2 — inside function
Step 4
```

## Calling Multiple Times

A function can be called as many times as you need:

```python
def say_hi():
    print("Hi!")

say_hi()   # First call
say_hi()   # Second call
say_hi()   # Third call
```

## Key Points

- Call a function by writing its name with `()`
- Python skips the function body during definition
- Code inside the function runs only when called
- A function can be called as many times as needed
- The function must be defined **before** you call it
