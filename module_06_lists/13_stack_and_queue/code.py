# ============================================
# MODULE 6 - SUBTOPIC 13: List as Stack & Queue
# ============================================
from collections import deque

# =============================
# 1. STACK (LIFO — Last In, First Out)
# =============================

# --- Example 1: Basic stack operations ---
stack = []
print("--- Stack (LIFO) ---")

# Push items
stack.append("A")
print(f"Push A: {stack}")
stack.append("B")
print(f"Push B: {stack}")
stack.append("C")
print(f"Push C: {stack}")

# Pop items (last in, first out)
item = stack.pop()
print(f"Pop: {item} → {stack}")   # C
item = stack.pop()
print(f"Pop: {item} → {stack}")   # B
item = stack.pop()
print(f"Pop: {item} → {stack}")   # A

# --- Example 2: Peek at top without removing ---
stack = [10, 20, 30]
top = stack[-1]   # peek
print(f"\nStack: {stack}")
print(f"Top (peek): {top}")   # 30

# --- Example 3: Check if stack is empty ---
stack = []
if len(stack) == 0:
    print("\nStack is empty!")

stack.append(42)
if len(stack) > 0:
    print(f"Stack has {len(stack)} item(s)")

# --- Example 4: Reverse a string using a stack ---
text = "Hello"
char_stack = []
for char in text:
    char_stack.append(char)

reversed_text = ""
while len(char_stack) > 0:
    reversed_text += char_stack.pop()
print(f"\nReversed '{text}': '{reversed_text}'")

# --- Example 5: Bracket matching ---
expression = "((1+2)*(3+4))"
bracket_stack = []
balanced = True

for char in expression:
    if char == "(":
        bracket_stack.append(char)
    elif char == ")":
        if len(bracket_stack) == 0:
            balanced = False
            break
        bracket_stack.pop()

if len(bracket_stack) > 0:
    balanced = False

print(f"\n'{expression}' brackets balanced? {balanced}")   # True

# --- Example 6: Undo history ---
print("\n--- Undo History ---")
document = "Hello"
undo_stack = [document]
print(f"Initial: '{document}'")

document = document + " World"
undo_stack.append(document)
print(f"Edit 1: '{document}'")

document = document + "!"
undo_stack.append(document)
print(f"Edit 2: '{document}'")

# Undo last edit
undo_stack.pop()   # remove current
document = undo_stack[-1]
print(f"After undo: '{document}'")

# =============================
# 2. QUEUE (FIFO — First In, First Out)
# =============================

# --- Example 7: Basic queue with list ---
print("\n--- Queue (FIFO) with list ---")
queue = []

# Enqueue
queue.append("Trush")
print(f"Enqueue Trush: {queue}")
queue.append("Rahul")
print(f"Enqueue Rahul: {queue}")
queue.append("Priya")
print(f"Enqueue Priya: {queue}")

# Dequeue (first in, first out)
person = queue.pop(0)
print(f"Dequeue: {person} → {queue}")   # Trush
person = queue.pop(0)
print(f"Dequeue: {person} → {queue}")   # Rahul

# --- Example 8: Print queue simulation ---
print("\n--- Print Queue ---")
print_queue = ["Document1.pdf", "Photo.jpg", "Report.doc"]
print(f"Print queue: {print_queue}")
while len(print_queue) > 0:
    current = print_queue.pop(0)
    print(f"  Printing: {current}")
    print(f"  Remaining: {print_queue}")

# =============================
# 3. DEQUE (Efficient Queue)
# =============================

# --- Example 9: Basic deque ---
print("\n--- deque (efficient queue) ---")
q = deque()
q.append("Trush")
q.append("Rahul")
q.append("Priya")
print(f"Queue: {list(q)}")

first = q.popleft()   # fast!
print(f"Popleft: {first} → {list(q)}")

# --- Example 10: Deque as double-ended queue ---
d = deque([1, 2, 3])
print(f"\nDeque: {list(d)}")

d.append(4)         # add to right
print(f"Append 4: {list(d)}")

d.appendleft(0)     # add to left
print(f"Appendleft 0: {list(d)}")

d.pop()              # remove from right
print(f"Pop: {list(d)}")

d.popleft()          # remove from left
print(f"Popleft: {list(d)}")

# --- Example 11: Deque with maxlen ---
recent = deque(maxlen=3)
for item in ["a", "b", "c", "d", "e"]:
    recent.append(item)
    print(f"  Added '{item}': {list(recent)}")
# Only keeps last 3!

# =============================
# 4. COMPARISON
# =============================

# --- Example 12: Stack vs Queue behavior ---
print("\n--- Stack vs Queue ---")
items = ["first", "second", "third"]

# Stack behavior
stack = items.copy()
print("Stack order (LIFO):")
while len(stack) > 0:
    print(f"  → {stack.pop()}")

# Queue behavior
queue = deque(items)
print("Queue order (FIFO):")
while len(queue) > 0:
    print(f"  → {queue.popleft()}")

# --- Example 13: Task processing (queue pattern) ---
print("\n--- Task Processor ---")
tasks = deque(["Send email", "Update database", "Generate report"])
completed = []
while len(tasks) > 0:
    task = tasks.popleft()
    print(f"  Processing: {task}")
    completed.append(task)
print(f"Completed: {completed}")

# ============================================
# TRY IT YOURSELF:
# 1. Use a stack to reverse the list [1, 2, 3, 4, 5]
# 2. Simulate a queue at a coffee shop with 5 customers
# 3. Use a deque with maxlen=5 to track the last 5 items
# ============================================
