# Practical Control Flow Patterns

This subtopic covers real-world patterns that combine everything from Module 4 into useful programs.

## Input Validation Loop

Keep asking until the user gives valid input:

```python
# Keep asking until a positive number is entered
value = -1
while value < 0:
    value = int(input("Enter a positive number: "))
    if value < 0:
        print("Invalid! Try again.")
print("You entered:", value)
```

## Menu-Driven Program

Show a menu and let the user pick options:

```python
choice = ""
while choice != "3":
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice")
```

## Sentinel-Controlled Loop

Use a **sentinel value** (special value) to signal when to stop:

```python
# Keep adding numbers until user enters 0 (sentinel)
total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Total:", total)
```

The sentinel (0) is not part of the data — it just signals "stop".

## Key Points

- **Input validation**: repeat until input meets requirements
- **Menu-driven**: show options in a loop, handle each choice
- **Sentinel-controlled**: use a special value to signal end of input
- These patterns combine `while`, `if-elif-else`, and `break`
