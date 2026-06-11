# ============================================
# MODULE 4 - SUBTOPIC 12: Practical Control Flow Patterns
# ============================================
# NOTE: Examples with input() are commented out so the file
# can run without user interaction. Uncomment to try them!

# =============================
# PATTERN 1: Input Validation
# =============================

# --- Example 1: Validate positive number (simulated) ---
# In real code you would use input(), but we simulate it here:
values_to_try = [(-5, "Invalid!"), (-1, "Invalid!"), (10, "Valid!")]
for value, expected in values_to_try:
    if value > 0:
        print("Accepted:", value)
    else:
        print("Rejected:", value, "— must be positive")

# --- Example 2: Input validation loop (commented — needs user) ---
# value = -1
# while value < 0:
#     value = int(input("Enter a positive number: "))
#     if value < 0:
#         print("Invalid! Must be positive. Try again.")
# print("You entered:", value)

# --- Example 3: Password validation (simulated) ---
correct_password = "python123"
attempts = 0
max_attempts = 3

# Simulating wrong attempts then correct
passwords_tried = ["wrong1", "wrong2", "python123"]
for password in passwords_tried:
    attempts += 1
    if password == correct_password:
        print("Login successful on attempt", attempts)
        break
    else:
        print("Wrong password. Attempt", attempts, "of", max_attempts)
        if attempts >= max_attempts:
            print("Account locked!")
            break

# =============================
# PATTERN 2: Menu-Driven Program
# =============================

# --- Example 4: Simple calculator menu (simulated) ---
print("\n--- Simple Calculator ---")
choices = ["1", "2", "5", "4"]  # simulated user choices

for choice in choices:
    print("\n--- MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")
    print("User chose:", choice)

    if choice == "1":
        a = 10
        b = 5
        print("Result:", a, "+", b, "=", a + b)
    elif choice == "2":
        a = 10
        b = 5
        print("Result:", a, "-", b, "=", a - b)
    elif choice == "3":
        a = 10
        b = 5
        print("Result:", a, "*", b, "=", a * b)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

# --- Example 5: Real menu (commented — needs user) ---
# choice = ""
# while choice != "3":
#     print("\n1. Greet")
#     print("2. Count to 5")
#     print("3. Quit")
#     choice = input("Choose: ")
#     if choice == "1":
#         print("Hello, Trush!")
#     elif choice == "2":
#         for i in range(1, 6):
#             print(i)
#     elif choice == "3":
#         print("Bye!")
#     else:
#         print("Invalid choice")

# =============================
# PATTERN 3: Sentinel-Controlled Loop
# =============================

# --- Example 6: Sum until sentinel (simulated) ---
# Sentinel value = -1 (signals "stop")
numbers = [10, 20, 30, 15, 5, -1, 100]   # -1 is the sentinel
total = 0
for num in numbers:
    if num == -1:
        break
    total += num
print("\nSum (until sentinel -1):", total)   # 80

# --- Example 7: Processing until "quit" ---
commands = ["save", "load", "print", "quit", "delete"]
for cmd in commands:
    if cmd == "quit":
        print("Quitting...")
        break
    print("Processing command:", cmd)
# Output: Processing: save, load, print, then Quitting...

# --- Example 8: Real sentinel loop (commented — needs user) ---
# total = 0
# count = 0
# print("Enter numbers (0 to stop):")
# num = int(input("> "))
# while num != 0:
#     total += num
#     count += 1
#     num = int(input("> "))
# if count > 0:
#     print("Total:", total)
#     print("Average:", total / count)
# else:
#     print("No numbers entered")

# =============================
# PATTERN 4: Combined Patterns
# =============================

# --- Example 9: Number guessing game (simulated) ---
secret = 42
guesses = [20, 50, 42]
attempt = 0
for guess in guesses:
    attempt += 1
    print("\nAttempt", attempt, "- Guess:", guess)
    if guess == secret:
        print("Correct! You got it in", attempt, "attempts!")
        break
    elif guess < secret:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")
else:
    print("Out of guesses! The number was", secret)

# --- Example 10: Grade processor ---
# Process student scores until done
scores = [85, 92, 78, 65, 95, 43, 88]
pass_count = 0
fail_count = 0
total = 0

for score in scores:
    total += score
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\n--- Grade Report ---")
print("Students:", len(scores))
print("Passed:", pass_count)
print("Failed:", fail_count)
print("Average:", total / len(scores))

# --- Example 11: FizzBuzz (classic pattern) ---
print("\n--- FizzBuzz (1-20) ---")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# --- Example 12: Finding prime numbers in a range ---
print("\n--- Prime Numbers (1-50) ---")
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a menu with options: "add", "subtract", "quit"
# 2. Write a number guessing game (use input() and a while loop)
# 3. Process a list of temperatures — count how many are above average
# ============================================
