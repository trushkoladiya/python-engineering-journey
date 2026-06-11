# Function Composition

**Function composition** means combining small functions together so the output of one becomes the input of the next — like a **pipeline**.

## The Idea

Instead of writing:

```python
result = func3(func2(func1(data)))
```

You build a pipeline:

```python
pipeline = compose(func1, func2, func3)
result = pipeline(data)
```

## Simple Composition

```python
def double(x):
    return x * 2

def add_one(x):
    return x + 1

# Manual composition
result = add_one(double(5))   # double(5)=10, add_one(10)=11

# As a pipeline
def compose(f, g):
    def combined(x):
        return g(f(x))
    return combined

double_then_add = compose(double, add_one)
print(double_then_add(5))   # 11
```

## Building Pipelines

```python
from functools import reduce

def pipeline(*functions):
    """Chain multiple functions into one."""
    def apply(value, func):
        return func(value)
    def composed(x):
        return reduce(apply, functions, x)
    return composed

process = pipeline(
    str.strip,
    str.lower,
    str.title,
)

print(process("  hello WORLD  "))   # "Hello World"
```

## Key Points

- Composition chains functions: output → input → output
- Small, focused functions compose better than large ones
- Pipelines make data transformations clear and readable
- Use `reduce()` to compose an arbitrary number of functions
