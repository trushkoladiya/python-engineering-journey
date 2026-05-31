# Nested Conditions

Nested conditions are `if` statements **inside other `if` statements**. They let you make decisions within decisions.

## Basic Syntax

```python
if outer_condition:
    if inner_condition:
        # runs when BOTH conditions are True
```

Each nested `if` adds another level of indentation.

## Simple Example

```python
age = 21
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Show your ID first")
else:
    print("Too young to enter")
```

## Multi-Level Nesting

You can nest multiple levels deep:

```python
num = 15
if num > 0:
    if num > 10:
        if num > 100:
            print("Very large")
        else:
            print("Medium")      # Medium
    else:
        print("Small positive")
else:
    print("Zero or negative")
```

## When to Use Nested Conditions

Use nesting when a second decision **only makes sense** after the first:

```python
is_member = True
purchase = 500

if is_member:
    if purchase > 1000:
        discount = 20
    else:
        discount = 10
else:
    discount = 0
print("Discount:", discount, "%")    # Discount: 10 %
```

## Key Points

- Nested `if` = an `if` inside another `if`
- Each level needs deeper indentation
- The inner `if` only runs when the outer condition is `True`
- Don't nest too deep — 2-3 levels is usually the maximum for readability
- Sometimes `and` / `or` can replace simple nesting (covered in next subtopic)
