# Dictionary Iteration

There are several ways to loop through dictionaries.

## Looping Over Keys (Default)

```python
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
for key in person:
    print(key)   # name, age, city
```

## Looping Over Values

```python
for value in person.values():
    print(value)   # Trush, 21, Mumbai
```

## Looping Over Key-Value Pairs

```python
for key, value in person.items():
    print(f"{key}: {value}")
```

## Key Points

- `for key in dict` iterates over keys (default)
- `for value in dict.values()` iterates over values
- `for key, value in dict.items()` iterates over both
- Most common pattern is `items()` for accessing both key and value
