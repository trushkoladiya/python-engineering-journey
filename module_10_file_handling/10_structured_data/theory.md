# Working with Structured Data

Real-world files often contain structured data like tables or records.

## Reading Line-by-Line and Parsing

```python
# File: students.txt
# Trush,21,92
# Rahul,22,85

with open("students.txt", "r") as file:
    for line in file:
        name, age, score = line.strip().split(",")
        print(f"{name}: age {age}, score {score}")
```

## Intro to CSV Handling

CSV (Comma-Separated Values) is a common format. Python has a built-in `csv` module:

```python
import csv

# Writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Score"])
    writer.writerow(["Trush", 21, 92])

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## Key Points

- Use `.strip().split(",")` for simple parsing
- Use the `csv` module for proper CSV handling
- `newline=""` is required when writing CSV on Windows
- CSV handles edge cases (commas in values, quotes) better than manual parsing
