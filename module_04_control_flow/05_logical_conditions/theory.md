# Logical Conditions in Control Flow

You can combine multiple conditions using **logical operators**: `and`, `or`, and `not`. This lets you write powerful conditions without deep nesting.

## Using `and`

Both conditions must be `True`:

```python
age = 21
has_id = True
if age >= 18 and has_id:
    print("Access granted")    # both True → prints
```

## Using `or`

At least one condition must be `True`:

```python
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")   # prints
```

## Using `not`

Reverses a boolean value:

```python
is_blocked = False
if not is_blocked:
    print("User can proceed")   # not False = True → prints
```

## Combining Multiple Operators

```python
age = 21
is_student = True
has_coupon = False

if age < 25 and (is_student or has_coupon):
    print("Discount applied")   # prints
```

Use **parentheses** to control evaluation order — `and` has higher priority than `or`.

## Short-Circuit Behavior

Python stops evaluating as soon as the result is determined:

- `and` → if the first condition is `False`, Python skips the second (result is already `False`)
- `or` → if the first condition is `True`, Python skips the second (result is already `True`)

```python
x = 0
# Python sees x != 0 is False, so it skips the division entirely
if x != 0 and 10 / x > 2:
    print("Valid")
else:
    print("Skipped safely")    # no division by zero error!
```

## Key Points

- `and` → both must be True
- `or` → at least one must be True
- `not` → reverses True/False
- Use `()` to group conditions clearly
- Short-circuit: Python stops early when the answer is already known
