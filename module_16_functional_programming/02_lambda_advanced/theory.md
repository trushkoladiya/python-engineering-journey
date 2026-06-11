# Lambda Functions (Advanced Usage)

A **lambda** is a small, anonymous function written in one line. You learned the basics in Module 8 — now we'll explore advanced patterns.

## Quick Recap

```python
# Regular function
def add(a, b):
    return a + b

# Same as lambda
add = lambda a, b: a + b
```

## Lambda in Complex Operations

### Sorting with Custom Keys

```python
students = [("Trush", 85), ("Rahul", 92), ("Eve", 78)]

# Sort by grade (second element)
sorted_students = sorted(students, key=lambda s: s[1])
# [('Eve', 78), ('Trush', 85), ('Rahul', 92)]
```

### Multiple Criteria Sorting

```python
data = [("Trush", 85), ("Rahul", 85), ("Eve", 92)]

# Sort by grade descending, then name ascending
result = sorted(data, key=lambda s: (-s[1], s[0]))
```

### Lambda with Conditional Logic

```python
classify = lambda x: "positive" if x > 0 else "non-positive"
print(classify(5))    # positive
print(classify(-3))   # non-positive
```

## When to Use Lambda

| Use Lambda | Use `def` |
|------------|-----------|
| Simple one-liner logic | Complex multi-line logic |
| Sorting keys | Functions that need docstrings |
| Quick callbacks | Reusable named functions |
| Inside `map()`, `filter()` | Functions with error handling |

## Key Points

- Lambda is best for **short, throwaway** functions
- Great for sort keys and data transformations
- If the logic is complex, use a regular `def` instead
- Lambda can only contain a **single expression** (no statements)
