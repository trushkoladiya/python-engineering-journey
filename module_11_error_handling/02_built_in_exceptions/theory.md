# Built-in Exceptions

Python has many **built-in exception types**. Each one describes a specific kind of error.

## Most Common Exceptions

### ValueError
A function receives a value of the right type but **wrong content**.

```python
int("hello")    # ValueError: invalid literal for int()
int("3.14")     # ValueError: cannot convert float string with int()
```

### TypeError
An operation is applied to the **wrong type**.

```python
"hello" + 5     # TypeError: can only concatenate str to str
len(42)         # TypeError: object of type 'int' has no len()
```

### IndexError
You access a **list/tuple index** that doesn't exist.

```python
items = [10, 20, 30]
items[5]        # IndexError: list index out of range
```

### KeyError
You access a **dictionary key** that doesn't exist.

```python
data = {"name": "Trush"}
data["age"]     # KeyError: 'age'
```

### ZeroDivisionError
You **divide by zero**.

```python
10 / 0          # ZeroDivisionError: division by zero
```

### FileNotFoundError
You try to open a **file that doesn't exist**.

```python
open("nonexistent.txt")  # FileNotFoundError
```

### AttributeError
You access an **attribute or method** that doesn't exist on an object.

```python
"hello".append("!")  # AttributeError: 'str' has no attribute 'append'
```

### NameError
You use a **variable that hasn't been defined**.

```python
print(undefined_var)  # NameError: name 'undefined_var' is not defined
```

## Exception Hierarchy (Simplified)

All exceptions inherit from `BaseException`. The most common ones are under `Exception`:

```
BaseException
└── Exception
    ├── ValueError
    ├── TypeError
    ├── IndexError
    ├── KeyError
    ├── ZeroDivisionError
    ├── FileNotFoundError
    ├── AttributeError
    ├── NameError
    └── ... many more
```

## Key Points

- Each exception type describes a **specific** kind of error
- Knowing the exception type helps you **fix bugs faster**
- You can **catch specific exceptions** to handle them differently (next subtopic)
