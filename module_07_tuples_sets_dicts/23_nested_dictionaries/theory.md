# Nested Dictionaries

A dictionary can contain other dictionaries as values, creating a multi-level data structure.

## Creating Nested Dictionaries

```python
students = {
    "Trush": {"age": 21, "grade": "A", "city": "Mumbai"},
    "Rahul": {"age": 21, "grade": "B", "city": "Delhi"},
}
```

## Accessing Nested Data

Use chained square brackets:

```python
print(students["Trush"]["grade"])   # A
print(students["Rahul"]["city"])      # Delhi
```

## Modifying Nested Data

```python
students["Trush"]["grade"] = "A+"
students["Rahul"]["email"] = "rahul@example.com"
```

## Safe Nested Access

```python
grade = students.get("Charlie", {}).get("grade", "N/A")
print(grade)   # N/A
```

## Key Points

- Nest dicts by using a dict as a value
- Access with chained keys: `dict[key1][key2]`
- Modify nested values the same way
- Use `.get()` for safe access to avoid `KeyError`
