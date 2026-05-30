# Ternary (Conditional) Operator

The ternary operator lets you write a simple **if-else in one line**. It picks one of two values based on a condition.

## Syntax

```python
value_if_true if condition else value_if_false
```

## How It Works

1. Python checks the **condition**
2. If `True` → returns the **left** value
3. If `False` → returns the **right** value

```python
age = 21
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

## Simple Examples

```python
x = 10
result = "positive" if x > 0 else "not positive"
print(result)   # positive

temperature = 35
weather = "hot" if temperature > 30 else "cool"
print(weather)  # hot
```

## Using Directly in print()

You don't need to store it in a variable:

```python
score = 85
print("Pass" if score >= 60 else "Fail")   # Pass
```

## With Numbers

```python
a = 10
b = 20
bigger = a if a > b else b
print(bigger)   # 20
```

## Nested Ternary (Use Carefully)

You can nest them, but keep it simple:

```python
x = 0
result = "positive" if x > 0 else ("zero" if x == 0 else "negative")
print(result)   # zero
```

> Nested ternaries can be hard to read — use them sparingly.

## Key Points

- Syntax: `value_if_true if condition else value_if_false`
- Returns one of two values based on a condition
- Great for simple choices in one line
- Avoid deep nesting — keep it readable
