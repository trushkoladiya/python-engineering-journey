# Strings (Deep Foundation)

## 1. String Creation

Strings can be created with single, double, or triple quotes.

```python
s1 = 'hello'
s2 = "hello"
s3 = '''This is
a multi-line string'''
s4 = """Also multi-line"""
```

## 2. Indexing

Each character has a position (index), starting from `0`.

```python
name = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5
```

```python
print(name[0])   # P
print(name[3])   # h
```

### Negative indexing (from the end)

```python
print(name[-1])  # n (last character)
print(name[-2])  # o
```

## 3. Slicing

Extract a portion of a string: `string[start:end:step]`

```python
text = "Python"
print(text[0:3])   # Pyt (index 0, 1, 2 — end is excluded)
print(text[2:])    # thon (from index 2 to end)
print(text[:4])    # Pyth (from start to index 3)
print(text[::2])   # Pto (every 2nd character)
print(text[::-1])  # nohtyP (reversed)
```

## 4. Immutability

Strings **cannot be changed** after creation.

```python
name = "Trush"
# name[0] = "K"  ❌ Error — strings are immutable
```

You must create a **new** string instead.

## 5. Concatenation & Repetition

```python
# Joining strings
greeting = "Hello" + " " + "World"

# Repeating strings
line = "-" * 20   # "--------------------"
```

## 6. Basic String Methods

```python
msg = "Hello World"
print(msg.upper())       # HELLO WORLD
print(msg.lower())       # hello world
print(msg.replace("World", "Python"))  # Hello Python
print(msg.count("l"))    # 3
print(len(msg))          # 11
```

## Key Points

- Use `[]` to access characters by index
- Slicing: `[start:end:step]` — end is excluded
- Strings are immutable (can't change in place)
- `+` joins, `*` repeats
- `len()` gives the length
