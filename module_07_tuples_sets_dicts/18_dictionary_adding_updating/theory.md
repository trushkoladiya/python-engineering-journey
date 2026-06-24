# Adding & Updating Dictionary Data

Dictionaries are mutable — you can add new key-value pairs and update existing ones.

## Adding New Key-Value Pairs

Simply assign a value to a new key:

```python
person = {"name": "Trush"}
person["age"] = 21
person["city"] = "Mumbai"
print(person)   # {'name': 'Trush', 'age': 21, 'city': 'Mumbai'}
```

## Updating Existing Values

Assign a new value to an existing key:

```python
person = {"name": "Trush", "age": 21}
person["age"] = 22
print(person)   # {'name': 'Trush', 'age': 22}
```

## `update()` Method

Update multiple key-value pairs at once:

```python
person = {"name": "Trush", "age": 21}
person.update({"age": 22, "city": "Mumbai"})
print(person)   # {'name': 'Trush', 'age': 22, 'city': 'Mumbai'}
```

## Key Points

- `dict[key] = value` adds if key is new, updates if key exists
- `update()` can add/update multiple pairs at once
- `update()` accepts dicts, lists of tuples, or keyword arguments
