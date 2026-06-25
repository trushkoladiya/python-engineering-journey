# Dictionary Methods

Three essential methods to view dictionary contents: `keys()`, `values()`, and `items()`.

## `keys()` — Get All Keys

```python
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print(person.keys())   # dict_keys(['name', 'age', 'city'])
```

## `values()` — Get All Values

```python
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print(person.values())   # dict_values(['Trush', 21, 'Mumbai'])
```

## `items()` — Get All Key-Value Pairs

Returns pairs as tuples:

```python
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print(person.items())
# dict_items([('name', 'Trush'), ('age', 21), ('city', 'Mumbai')])
```

## Converting to Lists

```python
keys_list = list(person.keys())
values_list = list(person.values())
items_list = list(person.items())
```

## Key Points

- `keys()` returns all keys
- `values()` returns all values
- `items()` returns key-value pairs as tuples
- These return **view objects** — convert with `list()` if needed
