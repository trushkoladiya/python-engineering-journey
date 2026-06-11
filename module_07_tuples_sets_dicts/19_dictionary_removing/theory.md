# Removing Dictionary Elements

Several ways to remove key-value pairs from a dictionary.

## `pop()` — Remove by Key

Returns the value and removes the key:

```python
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
age = person.pop("age")
print(age)       # 21
print(person)    # {'name': 'Trush', 'city': 'Mumbai'}
```

With a default (no error if missing):

```python
email = person.pop("email", "not found")
print(email)   # not found
```

## `popitem()` — Remove Last Item

Removes and returns the last inserted key-value pair:

```python
d = {"a": 1, "b": 2, "c": 3}
last = d.popitem()
print(last)   # ('c', 3)
print(d)      # {'a': 1, 'b': 2}
```

## `del` — Delete by Key

```python
person = {"name": "Trush", "age": 21}
del person["age"]
print(person)   # {'name': 'Trush'}
```

## `clear()` — Remove All

```python
data = {"a": 1, "b": 2}
data.clear()
print(data)   # {}
```

## Key Points

- `pop(key)` removes and returns the value (with optional default)
- `popitem()` removes the last inserted item
- `del dict[key]` removes a key-value pair
- `clear()` empties the entire dictionary
