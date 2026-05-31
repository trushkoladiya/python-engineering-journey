# if-elif-else Ladder

When you have **more than two possible outcomes**, use `elif` (short for "else if") to check multiple conditions one by one.

## Basic Syntax

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
elif condition3:
    # runs if both above are False AND condition3 is True
else:
    # runs if ALL conditions above are False
```

## Simple Example

```python
marks = 72
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)    # Grade: C
```

## Order of Evaluation

Python checks conditions **from top to bottom** and stops at the **first True** condition:

```python
score = 95
if score >= 60:
    print("Pass")        # This prints! (first True match)
elif score >= 90:
    print("Excellent")   # Never reached — even though it's True
```

**Important**: Put the most specific condition first, or the most restrictive.

## Fallback Logic (else)

The `else` at the end is optional but acts as a **catch-all**:

```python
day = "Sunday"
if day == "Monday":
    print("Start of work week")
elif day == "Friday":
    print("Almost weekend!")
elif day == "Saturday":
    print("Weekend!")
else:
    print("Regular day")   # catches everything else
```

## Key Points

- `elif` lets you check multiple conditions in sequence
- Only the **first True** block runs — the rest are skipped
- `else` is optional — catches anything not matched above
- Order matters — put the most specific/restrictive conditions first
- You can have as many `elif` blocks as needed
