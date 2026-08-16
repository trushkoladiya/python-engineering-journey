# ============================================
# MODULE 18 - SUBTOPIC 15: Testing
# ============================================

# Writing unit tests to verify your code works correctly.

import unittest
import sys

# =============================
# FUNCTIONS TO TEST
# =============================

def add(a, b):
    """Add two numbers."""
    return a + b

def divide(a, b):
    """Divide a by b. Raises ValueError for zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_palindrome(text):
    """Check if text is a palindrome (case-insensitive)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def find_max(numbers):
    """Find the maximum value in a list."""
    if not numbers:
        raise ValueError("Empty list has no maximum")
    result = numbers[0]
    for num in numbers:
        if num > result:
            result = num
    return result

def fizzbuzz(n):
    """Return FizzBuzz result for a number."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

# =============================
# 1. BASIC TEST CLASS
# =============================

class TestAdd(unittest.TestCase):
    """Tests for the add function."""

    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_mixed_numbers(self):
        self.assertEqual(add(-1, 5), 4)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)


# =============================
# 2. TESTING EXCEPTIONS
# =============================

class TestDivide(unittest.TestCase):
    """Tests for the divide function."""

    def test_normal_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_float_result(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=3)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_by_zero_message(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("zero", str(context.exception))

    def test_negative_division(self):
        self.assertEqual(divide(-10, 2), -5)


# =============================
# 3. TESTING WITH MULTIPLE ASSERTIONS
# =============================

class TestPalindrome(unittest.TestCase):
    """Tests for the is_palindrome function."""

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_case_insensitive(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome("was it a car or a cat i saw"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


# =============================
# 4. TESTING WITH setUp
# =============================

class TestFindMax(unittest.TestCase):
    """Tests for find_max with setUp."""

    def setUp(self):
        """Run before EACH test method."""
        self.positive_list = [3, 7, 2, 9, 4]
        self.negative_list = [-5, -1, -8, -3]
        self.mixed_list = [-2, 0, 5, -3, 8]
        self.single_list = [42]

    def test_positive_numbers(self):
        self.assertEqual(find_max(self.positive_list), 9)

    def test_negative_numbers(self):
        self.assertEqual(find_max(self.negative_list), -1)

    def test_mixed_numbers(self):
        self.assertEqual(find_max(self.mixed_list), 8)

    def test_single_element(self):
        self.assertEqual(find_max(self.single_list), 42)

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            find_max([])

    def test_duplicates(self):
        self.assertEqual(find_max([5, 5, 5]), 5)


# =============================
# 5. TESTING FizzBuzz
# =============================

class TestFizzBuzz(unittest.TestCase):
    """Tests for FizzBuzz logic."""

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_regular_numbers(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(7), "7")


# =============================
# 6. TESTING A CLASS
# =============================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __repr__(self):
        return f"BankAccount({self.owner}, ${self.balance})"


class TestBankAccount(unittest.TestCase):
    """Tests for BankAccount class."""

    def setUp(self):
        self.account = BankAccount("Trush", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_negative_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_zero_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_multiple_operations(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.deposit(25)
        self.assertEqual(self.account.balance, 175)


# =============================
# 7. ASSERT METHODS REFERENCE
# =============================

class TestAssertMethods(unittest.TestCase):
    """Demonstrating various assert methods."""

    def test_equal(self):
        self.assertEqual(1 + 1, 2)

    def test_not_equal(self):
        self.assertNotEqual(1, 2)

    def test_true(self):
        self.assertTrue(10 > 5)

    def test_false(self):
        self.assertFalse(10 < 5)

    def test_is_none(self):
        self.assertIsNone(None)

    def test_is_not_none(self):
        self.assertIsNotNone("hello")

    def test_in(self):
        self.assertIn(3, [1, 2, 3, 4])

    def test_not_in(self):
        self.assertNotIn(5, [1, 2, 3, 4])

    def test_is_instance(self):
        self.assertIsInstance("hello", str)

    def test_almost_equal(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=10)


# =============================
# RUN ALL TESTS
# =============================

if __name__ == "__main__":
    # Run tests with verbose output
    print("=== Running All Tests ===")
    print()

    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    test_classes = [
        TestAdd, TestDivide, TestPalindrome,
        TestFindMax, TestFizzBuzz, TestBankAccount,
        TestAssertMethods
    ]

    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))

    # Run with verbosity
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)

    print()
    print(f"  Tests run: {result.testsRun}")
    print(f"  Failures: {len(result.failures)}")
    print(f"  Errors: {len(result.errors)}")
    print(f"  Success: {result.wasSuccessful()}")
    print()

    # ============================================
    # TRY IT YOURSELF:
    # 1. Write tests for a function that checks if
    #    a number is prime
    # 2. Write tests for a Stack class (push, pop, peek)
    # 3. Write tests for a function that parses CSV lines
    # ============================================
