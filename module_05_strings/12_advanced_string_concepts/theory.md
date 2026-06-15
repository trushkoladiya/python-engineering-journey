# Advanced String Concepts

This covers string comparison, Unicode basics, and the `ord()` / `chr()` functions.

## String Comparison (Lexicographic)

Python compares strings **character by character** using their Unicode values:

```python
print("apple" < "banana")    # True — 'a' comes before 'b'
print("apple" < "apricot")   # True — same first two, 'p' < 'r'
print("abc" == "abc")        # True — identical
```

Uppercase letters have **smaller** values than lowercase:

```python
print("A" < "a")    # True — uppercase comes before lowercase
print("Z" < "a")    # True — all uppercase before all lowercase
```

## `ord()` — Character to Number

Every character has a numeric code. `ord()` gives you this number:

```python
print(ord("A"))   # 65
print(ord("a"))   # 97
print(ord("0"))   # 48
print(ord(" "))   # 32
```

## `chr()` — Number to Character

`chr()` does the reverse — converts a number to its character:

```python
print(chr(65))    # A
print(chr(97))    # a
print(chr(48))    # 0
print(chr(32))    # (space)
```

## ASCII Basics

The first 128 characters form the **ASCII** table:
- `0-9` → codes 48–57
- `A-Z` → codes 65–90
- `a-z` → codes 97–122

## Unicode

Python strings support **Unicode**, which includes characters from all languages:

```python
print("\u0048\u0065\u006C\u006C\u006F")   # Hello
print("\u2764")   # ❤
```

## Key Points

- Strings are compared character by character (lexicographic order)
- `ord()` converts a character to its numeric code
- `chr()` converts a numeric code to its character
- Uppercase letters (`A-Z`) have smaller codes than lowercase (`a-z`)
- Python supports full Unicode (not just ASCII)
