# String Creation

Strings are sequences of characters. Python gives you several ways to create them.

## Single Quotes

```python
name = 'Trush'
print(name)   # Trush
```

## Double Quotes

```python
greeting = "Hello, World!"
print(greeting)   # Hello, World!
```

Single and double quotes work the same way. Use whichever you prefer.

## Mixing Quotes

If your string contains a quote character, use the **other** type of quote:

```python
message = "It's a great day"    # apostrophe inside double quotes
html = '<a href="link">Click</a>'   # double quotes inside single quotes
```

## Triple Quotes

Triple quotes (`'''` or `"""`) let you write strings that span **multiple lines**:

```python
poem = '''Roses are red,
Violets are blue,
Python is great,
And so are you.'''
print(poem)
```

## Multi-line Strings

Triple-quoted strings preserve the line breaks exactly as you write them:

```python
address = """Trush Koladiya
42 MG Road
Ahmedabad, Gujarat 380001"""
print(address)
```

## Empty Strings

A string with nothing inside is called an empty string:

```python
empty = ""
print(empty)       # (prints nothing)
print(len(empty))  # 0
```

## Key Points

- Use `'...'` or `"..."` for single-line strings
- Use `'''...'''` or `"""..."""` for multi-line strings
- Mix quote types when your string contains quotes
- Empty strings have length 0
