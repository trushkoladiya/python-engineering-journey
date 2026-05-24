# Input & Output

## 1. `print()` — Output

`print()` displays information to the screen.

```python
print("Hello!")
print(42)
print(3.14)
```

### Printing multiple values

Use commas to print multiple things. Python adds a space between them.

```python
print("Age:", 25)        # Age: 25
print("A", "B", "C")    # A B C
```

### Changing the separator

```python
print("A", "B", "C", sep="-")   # A-B-C
print("A", "B", "C", sep="")    # ABC
```

### Changing the ending

By default, `print()` adds a newline at the end. You can change it:

```python
print("Hello", end=" ")
print("World")
# Output: Hello World (on one line)
```

## 2. Formatting Output

### String concatenation (joining)

```python
name = "Trush"
print("Hello, " + name + "!")  # Hello, Trush!
```

> You can only concatenate strings with strings, not strings with numbers.

### f-strings (formatted strings)

The easiest way to mix text and variables:

```python
name = "Trush"
age = 21
print(f"My name is {name} and I am {age} years old")
```

- Put `f` before the opening quote
- Use `{variable}` to insert values

## 3. `input()` — Getting User Input

`input()` waits for the user to type something and press Enter.

```python
name = input("What is your name? ")
print("Hello, " + name)
```

> `input()` **always returns a string**, even if the user types a number.

## 4. Type Casting Input

Since `input()` returns a string, you need to **convert** it for math:

```python
age = input("Enter your age: ")     # "25" — this is a string!
age = int(age)                       # 25 — now it's an integer
```

Shorter version:

```python
age = int(input("Enter your age: "))
```

## Key Points

- `print()` shows output
- Use `f""` strings to format output easily
- `input()` gets user input (always returns a string)
- Convert input with `int()` or `float()` for numbers
