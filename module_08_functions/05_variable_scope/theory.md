# Variable Scope

**Scope** determines where a variable can be accessed. Variables created inside a function are **local** — they only exist inside that function.

## Local Variables

A variable created inside a function is **local** to that function:

```python
def my_function():
    x = 10          # local variable
    print(x)        # ✅ Works inside function

my_function()
# print(x)         # ❌ Error — x doesn't exist outside
```

## Global Variables

A variable created outside all functions is **global**:

```python
name = "Trush"     # global variable

def greet():
    print(f"Hello, {name}!")   # ✅ Can read global

greet()
print(name)        # ✅ Works outside too
```

## The `global` Keyword

To **modify** a global variable inside a function, use `global`:

```python
count = 0

def increment():
    global count
    count = count + 1

increment()
print(count)   # 1
```

## Variable Shadowing

A local variable with the **same name** as a global one creates a separate copy:

```python
x = 100          # global

def my_func():
    x = 5         # local — shadows the global
    print(x)      # 5

my_func()
print(x)          # 100 — global unchanged
```

## Key Points

- Local variables exist only inside their function
- Global variables can be **read** inside functions
- Use `global` keyword to **modify** a global variable
- Same-named local variables **shadow** global ones
- Avoid excessive use of `global` — prefer parameters and return values
