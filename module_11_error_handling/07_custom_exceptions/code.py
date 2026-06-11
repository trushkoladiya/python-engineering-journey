# ============================================
# MODULE 11 - SUBTOPIC 7: Custom Exceptions
# ============================================

# Custom exceptions = your own error types.
# They inherit from Exception using a simple class pattern.
# (You'll learn classes fully in Module 12 — for now, follow this template.)

# =============================
# 1. BASIC CUSTOM EXCEPTION
# =============================

# --- Example 1: Simplest custom exception ---
print("=== Basic Custom Exception ===")
print()

# The pattern: class YourErrorName(Exception): pass
class InvalidAgeError(Exception):
    pass


try:
    age = -5
    if age < 0:
        raise InvalidAgeError(f"Age cannot be negative: {age}")
except InvalidAgeError as e:
    print(f"  Caught InvalidAgeError: {e}")

print()

# =============================
# 2. MULTIPLE CUSTOM EXCEPTIONS
# =============================

# --- Example 2: Several custom errors for a system ---
print("=== Multiple Custom Exceptions ===")
print()

class TooShortError(Exception):
    pass

class TooLongError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass


def validate_password(password):
    """Validate a password with custom exceptions."""
    if len(password) < 6:
        raise TooShortError(f"Password too short ({len(password)} chars, need 6+)")
    if len(password) > 20:
        raise TooLongError(f"Password too long ({len(password)} chars, max 20)")
    if " " in password:
        raise InvalidCharacterError("Password cannot contain spaces")
    return True


test_passwords = ["abc", "good_password", "this_is_way_too_long_for_a_password", "has space", "valid123"]

for pwd in test_passwords:
    try:
        validate_password(pwd)
        print(f"  '{pwd}' → Valid ✓")
    except TooShortError as e:
        print(f"  '{pwd}' → TooShortError: {e}")
    except TooLongError as e:
        print(f"  '{pwd}' → TooLongError: {e}")
    except InvalidCharacterError as e:
        print(f"  '{pwd}' → InvalidCharacterError: {e}")

print()

# =============================
# 3. CUSTOM EXCEPTIONS IN REAL SCENARIOS
# =============================

# --- Example 3: Bank account errors ---
print("=== Bank Account Errors ===")
print()

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class AccountLockedError(Exception):
    pass


def withdraw(balance, amount, is_locked):
    """Withdraw money with validation."""
    if is_locked:
        raise AccountLockedError("Account is locked — contact support")
    if amount <= 0:
        raise InvalidAmountError(f"Amount must be positive, got {amount}")
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw {amount} — balance is only {balance}"
        )
    return balance - amount


test_withdrawals = [
    (1000, 200, False),     # OK
    (1000, 2000, False),    # InsufficientFundsError
    (1000, -50, False),     # InvalidAmountError
    (1000, 100, True),      # AccountLockedError
    (500, 500, False),      # OK — exact balance
]

for balance, amount, locked in test_withdrawals:
    try:
        new_balance = withdraw(balance, amount, locked)
        print(f"  Withdraw {amount} from {balance} → New balance: {new_balance} ✓")
    except InsufficientFundsError as e:
        print(f"  Withdraw {amount} from {balance} → {e} ✗")
    except InvalidAmountError as e:
        print(f"  Withdraw {amount} from {balance} → {e} ✗")
    except AccountLockedError as e:
        print(f"  Withdraw {amount} from {balance} → {e} ✗")

print()

# =============================
# 4. CUSTOM EXCEPTIONS vs BUILT-IN
# =============================

# --- Example 4: Why custom is better than generic ---
print("=== Custom vs Built-in ===")
print()

# Using generic ValueError — unclear
def validate_score_generic(score):
    if score < 0 or score > 100:
        raise ValueError(f"Invalid score: {score}")
    return score


# Using custom exception — specific and clear
class InvalidScoreError(Exception):
    pass


def validate_score_custom(score):
    if score < 0:
        raise InvalidScoreError(f"Score cannot be negative: {score}")
    if score > 100:
        raise InvalidScoreError(f"Score cannot exceed 100: {score}")
    return score


test_scores = [85, -5, 150, 100, 0]

print("  Using custom InvalidScoreError:")
for score in test_scores:
    try:
        validate_score_custom(score)
        print(f"    Score {score}: valid ✓")
    except InvalidScoreError as e:
        print(f"    Score {score}: {e} ✗")

print()

# =============================
# 5. PRACTICAL: QUIZ SYSTEM ERRORS
# =============================

# --- Example 5: Complete system with custom exceptions ---
print("=== Quiz System ===")
print()

class EmptyAnswerError(Exception):
    pass

class InvalidQuestionError(Exception):
    pass

class QuizCompleteError(Exception):
    pass


def check_answer(question, answer, correct_answer, quiz_done):
    """Check a quiz answer with validation."""
    if quiz_done:
        raise QuizCompleteError("Quiz is already finished!")
    if not question:
        raise InvalidQuestionError("Question cannot be empty")
    if not answer or answer.strip() == "":
        raise EmptyAnswerError("Answer cannot be blank")
    return answer.strip().lower() == correct_answer.strip().lower()


quiz_tests = [
    ("What is 2+2?", "4", "4", False),          # Correct
    ("What is 3+3?", "7", "6", False),           # Wrong
    ("What is 5+5?", "", "10", False),           # EmptyAnswerError
    ("", "yes", "yes", False),                    # InvalidQuestionError
    ("What is 1+1?", "2", "2", True),            # QuizCompleteError
]

for question, answer, correct, done in quiz_tests:
    try:
        is_correct = check_answer(question, answer, correct, done)
        status = "Correct! ✓" if is_correct else "Wrong ✗"
        print(f"  Q: '{question}' A: '{answer}' → {status}")
    except EmptyAnswerError as e:
        print(f"  Q: '{question}' → EmptyAnswerError: {e}")
    except InvalidQuestionError as e:
        print(f"  Q: '(empty)' → InvalidQuestionError: {e}")
    except QuizCompleteError as e:
        print(f"  Q: '{question}' → QuizCompleteError: {e}")

# ============================================
# TRY IT YOURSELF:
# 1. Create an InvalidEmailError and use it in a validator
# 2. Create a NegativeNumberError for a math function
# 3. Build a system with 3+ custom exceptions
# ============================================
