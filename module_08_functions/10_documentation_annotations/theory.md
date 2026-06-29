# Documentation & Annotations

Good functions should be **documented** so others (and your future self) understand what they do.

## Docstrings

A **docstring** is a string placed on the first line inside a function. Use triple quotes:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

Multi-line docstring:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area (length * width)
    """
    return length * width
```

Access the docstring with `.__doc__` or `help()`:

```python
print(add.__doc__)
help(add)
```

## Type Hints (Introduction)

Type hints tell readers what types a function expects and returns:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b
```

Type hints are **optional** and don't enforce anything — they're for documentation.

## Key Points

- Use docstrings to explain what a function does
- Triple quotes `"""..."""` for docstrings
- Place docstrings as the **first line** inside the function
- Type hints show expected types: `param: type` and `-> return_type`
- Type hints don't enforce — they're documentation only
