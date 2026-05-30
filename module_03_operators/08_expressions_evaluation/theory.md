# Expressions & Evaluation

An **expression** is any piece of code that produces a value. Understanding how Python evaluates expressions is key to writing correct code.

## What is an Expression?

Anything that Python can **evaluate to a value** is an expression.

```python
# These are all expressions:
5 + 3          # evaluates to 8
10 > 5         # evaluates to True
"hi" + " there"  # evaluates to "hi there"
```

## Expressions vs Statements

- **Expression** — produces a value (`5 + 3` → `8`)
- **Statement** — performs an action (`x = 10` — assigns, doesn't produce a value by itself)

```python
x = 5 + 3    # "5 + 3" is the expression, the whole line is a statement
```

## Combining Multiple Operators

You can mix different operators in one expression:

```python
result = 10 + 5 * 2 - 3
print(result)   # 17  (multiplication first: 5*2=10, then 10+10-3=17)
```

## Nested Expressions

Expressions inside expressions — use parentheses for clarity:

```python
result = (10 + 5) * (2 - 3)
print(result)   # -15

inner = (3 + 4)
outer = inner * 2
print(outer)   # 14
```

## Evaluation Order

Python evaluates expressions following:

1. **Parentheses** `()` — always first
2. **Operator precedence** — which operator runs first
3. **Left to right** — when operators have equal precedence (associativity)

```python
# Same precedence: left to right
print(10 - 5 + 3)    # 8  (left to right: 5 + 3)
print(10 / 2 * 3)    # 15.0  (left to right: 5.0 * 3)
```

## Mixing Types in Expressions

Python auto-promotes types (learned in Module 2):

```python
print(5 + 3.0)        # 8.0  (int + float = float)
print(True + 5)       # 6    (True = 1)
print(False + 10)     # 10   (False = 0)
```

## Key Points

- An expression is code that produces a value
- Use parentheses to make order explicit
- Python follows precedence, then left-to-right
- Types get auto-promoted when mixed
