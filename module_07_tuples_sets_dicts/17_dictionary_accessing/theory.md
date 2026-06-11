# Accessing Dictionary Data

There are several ways to get values from a dictionary.

## Using Keys (Square Brackets)

```python
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print(person["name"])   # Trush
print(person["age"])    # 21
```

If the key doesn't exist, you get a `KeyError`:

```python
# print(person["email"])   # KeyError: 'email'
```

## Using `get()` — Safe Access

`get()` returns `None` instead of an error when the key is missing:

```python
person = {"name": "Trush", "age": 21}
print(person.get("name"))     # Trush
print(person.get("email"))    # None (no error!)
```

You can set a **default value**:

```python
print(person.get("email", "not provided"))   # not provided
```

## Handling Missing Keys Safely

Check before accessing:

```python
if "email" in person:
    print(person["email"])
else:
    print("No email found")
```

## Key Points

- `dict[key]` — fast but raises `KeyError` if missing
- `dict.get(key)` — returns `None` if missing (no error)
- `dict.get(key, default)` — returns default if missing
- Use `in` to check if a key exists before accessing
