# ============================================
# MODULE 17 - SUBTOPIC 14: Stack
# ============================================

# Stack: LIFO (Last In, First Out) data structure.
# Think of a stack of plates.

# =============================
# 1. STACK USING A LIST
# =============================

print("=== Stack Using a List ===")
print()

stack = []

# Push items
stack.append("A")
stack.append("B")
stack.append("C")
print(f"  After pushing A, B, C: {stack}")
print(f"  Top element: {stack[-1]}")

# Pop items (LIFO)
popped = stack.pop()
print(f"  Popped: {popped}")
print(f"  Stack now: {stack}")

popped = stack.pop()
print(f"  Popped: {popped}")
print(f"  Stack now: {stack}")
print()

# =============================
# 2. STACK CLASS
# =============================

print("=== Stack Class Implementation ===")
print()

class Stack:
    """Stack data structure using a list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add item to top."""
        self._items.append(item)

    def pop(self):
        """Remove and return top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """View top item without removing."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if stack is empty."""
        return len(self._items) == 0

    def size(self):
        """Return number of items."""
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(f"  Stack: {s}")
print(f"  Peek: {s.peek()}")
print(f"  Pop: {s.pop()}")
print(f"  Pop: {s.pop()}")
print(f"  Stack: {s}")
print(f"  Size: {s.size()}")
print(f"  Empty: {s.is_empty()}")
print()

# =============================
# 3. BALANCED PARENTHESES
# =============================

print("=== Balanced Parentheses ===")
print()

def is_balanced(expression):
    """Check if parentheses are balanced."""
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0

test_expressions = [
    "(())",
    "([{}])",
    "(()",
    "([)]",
    "{[()]}",
    ")()",
    "",
]

for expr in test_expressions:
    result = "✓ balanced" if is_balanced(expr) else "✗ not balanced"
    display = expr if expr else "(empty)"
    print(f"  '{display}' → {result}")
print()

# =============================
# 4. REVERSE A STRING USING STACK
# =============================

print("=== Reverse String Using Stack ===")
print()

def reverse_string(text):
    """Reverse a string using a stack."""
    stack = []
    for char in text:
        stack.append(char)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()
    return reversed_text

text = "Hello, World!"
print(f"  Original: '{text}'")
print(f"  Reversed: '{reverse_string(text)}'")
print()

# =============================
# 5. EVALUATE POSTFIX EXPRESSION
# =============================

print("=== Evaluate Postfix Expression ===")
print()

def evaluate_postfix(expression):
    """
    Evaluate a postfix (reverse Polish) expression.
    e.g., "3 4 + 2 *" = (3 + 4) * 2 = 14
    """
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in expression.split():
        if token in operators:
            b = stack.pop()   # second operand
            a = stack.pop()   # first operand
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]

expressions = [
    ("3 4 +", "(3 + 4)"),
    ("3 4 + 2 *", "(3 + 4) * 2"),
    ("5 1 2 + 4 * + 3 -", "5 + ((1 + 2) * 4) - 3"),
]

for postfix, infix in expressions:
    result = evaluate_postfix(postfix)
    print(f"  {postfix:25} = {infix:25} = {result}")
print()

# =============================
# 6. MIN STACK (GET MINIMUM IN O(1))
# =============================

print("=== Min Stack ===")
print()

class MinStack:
    """Stack that tracks minimum element in O(1)."""

    def __init__(self):
        self._items = []
        self._mins = []     # parallel stack tracking minimums

    def push(self, item):
        self._items.append(item)
        if not self._mins or item <= self._mins[-1]:
            self._mins.append(item)

    def pop(self):
        item = self._items.pop()
        if item == self._mins[-1]:
            self._mins.pop()
        return item

    def get_min(self):
        return self._mins[-1]

    def peek(self):
        return self._items[-1]

ms = MinStack()
operations = [("push", 5), ("push", 3), ("push", 7), ("push", 1), ("push", 4)]

for op, val in operations:
    ms.push(val)
    print(f"  Push {val} → min = {ms.get_min()}")

print()
for _ in range(3):
    popped = ms.pop()
    print(f"  Pop {popped} → min = {ms.get_min()}")
print()

# =============================
# 7. BROWSER HISTORY (STACK APPLICATION)
# =============================

print("=== Browser History Simulation ===")
print()

class BrowserHistory:
    """Simulate browser back/forward using two stacks."""

    def __init__(self):
        self._back_stack = []
        self._forward_stack = []
        self._current = None

    def visit(self, url):
        if self._current:
            self._back_stack.append(self._current)
        self._current = url
        self._forward_stack.clear()

    def back(self):
        if self._back_stack:
            self._forward_stack.append(self._current)
            self._current = self._back_stack.pop()
        return self._current

    def forward(self):
        if self._forward_stack:
            self._back_stack.append(self._current)
            self._current = self._forward_stack.pop()
        return self._current

browser = BrowserHistory()
browser.visit("google.com")
browser.visit("python.org")
browser.visit("github.com")
print(f"  Current: {browser._current}")

browser.back()
print(f"  Back: {browser._current}")

browser.back()
print(f"  Back: {browser._current}")

browser.forward()
print(f"  Forward: {browser._current}")

browser.visit("stackoverflow.com")
print(f"  Visit: {browser._current}")

result = browser.forward()
print(f"  Forward (nothing): {result}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use a stack to check if an HTML tag sequence
#    is properly nested (e.g., <div><p></p></div>)
# 2. Implement a function to convert infix to postfix
# 3. Use a stack to find the next greater element
#    for each item in a list
# ============================================
