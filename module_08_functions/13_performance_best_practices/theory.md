# Performance & Best Practices

Writing efficient functions is important for clean, maintainable code.

## Avoid Unnecessary Function Calls

Don't call a function repeatedly when you can store the result:

```python
# ❌ Bad — calling len() every iteration
for i in range(len(my_list)):
    print(my_list[i])

# ✅ Good — direct iteration
for item in my_list:
    print(item)
```

## Keep Functions Small

Each function should fit on one screen. If it's too long, break it into smaller functions.

## Reusability

Write functions that solve general problems, not specific ones:

```python
# ❌ Too specific
def add_tax_18(price):
    return price * 1.18

# ✅ General and reusable
def add_tax(price, rate=0.18):
    return price * (1 + rate)
```

## Avoid Side Effects When Possible

Functions that don't modify external state are easier to understand and test.

## Use Default Values Wisely

Default values reduce the number of arguments needed for common cases.

## Key Points

- Store results instead of recalculating
- Keep functions short and focused
- Write general, reusable functions
- Minimize side effects
- Use meaningful default values
