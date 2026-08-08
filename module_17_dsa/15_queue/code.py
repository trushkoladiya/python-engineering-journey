# ============================================
# MODULE 17 - SUBTOPIC 15: Queue
# ============================================

# Queue: FIFO (First In, First Out) data structure.
# Think of a line at a store.

from collections import deque
import time

# =============================
# 1. QUEUE USING A LIST (SIMPLE BUT SLOW)
# =============================

print("=== Queue Using a List ===")
print()

queue = []

# Enqueue (add to back)
queue.append("Trush")
queue.append("Rahul")
queue.append("Charlie")
print(f"  Queue: {queue}")

# Dequeue (remove from front) — O(n) with list!
served = queue.pop(0)
print(f"  Served: {served}")
print(f"  Queue: {queue}")
print()

# =============================
# 2. QUEUE USING DEQUE (EFFICIENT)
# =============================

print("=== Queue Using deque (Recommended) ===")
print()

queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")
print(f"  Queue: {list(queue)}")

# Dequeue — O(1) with deque!
processed = queue.popleft()
print(f"  Processed: {processed}")
print(f"  Queue: {list(queue)}")
print(f"  Front: {queue[0]}")
print(f"  Size: {len(queue)}")
print()

# =============================
# 3. LIST vs DEQUE — SPEED
# =============================

print("=== List vs Deque — Speed Comparison ===")
print()

size = 100_000

# List — pop(0) is O(n)
list_queue = list(range(size))
start = time.time()
while list_queue:
    list_queue.pop(0)
t_list = time.time() - start

# Deque — popleft() is O(1)
deque_queue = deque(range(size))
start = time.time()
while deque_queue:
    deque_queue.popleft()
t_deque = time.time() - start

print(f"  Dequeue {size:,} items:")
print(f"    List:  {t_list:.4f}s")
print(f"    Deque: {t_deque:.4f}s")
if t_deque > 0:
    print(f"    Deque is ~{t_list / t_deque:.0f}x faster!")
print()

# =============================
# 4. QUEUE CLASS
# =============================

print("=== Queue Class Implementation ===")
print()

class Queue:
    """Queue data structure using deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add item to back."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return front item."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        """View front item without removing."""
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"

q = Queue()
for item in ["A", "B", "C", "D"]:
    q.enqueue(item)
print(f"  Queue: {q}")
print(f"  Peek: {q.peek()}")
print(f"  Dequeue: {q.dequeue()}")
print(f"  Dequeue: {q.dequeue()}")
print(f"  Queue: {q}")
print()

# =============================
# 5. TASK SCHEDULER SIMULATION
# =============================

print("=== Task Scheduler ===")
print()

class TaskScheduler:
    """Simple FIFO task scheduler."""

    def __init__(self):
        self._queue = deque()

    def add_task(self, task_name, priority="normal"):
        self._queue.append({"name": task_name, "priority": priority})
        print(f"    Added: {task_name} ({priority})")

    def process_next(self):
        if self._queue:
            task = self._queue.popleft()
            print(f"    Processing: {task['name']} ({task['priority']})")
            return task
        print("    No tasks to process")
        return None

    def pending(self):
        return len(self._queue)

scheduler = TaskScheduler()
scheduler.add_task("Send email", "high")
scheduler.add_task("Update database", "normal")
scheduler.add_task("Generate report", "low")
scheduler.add_task("Backup files", "normal")

print(f"  Pending: {scheduler.pending()}")
print()
print("  Processing tasks:")
while scheduler.pending() > 0:
    scheduler.process_next()
print()

# =============================
# 6. HOT POTATO GAME (CIRCULAR QUEUE)
# =============================

print("=== Hot Potato Game ===")
print()

def hot_potato(names, count):
    """Simulate hot potato — last person standing wins."""
    queue = deque(names)

    while len(queue) > 1:
        # Pass the potato 'count' times
        for _ in range(count):
            queue.append(queue.popleft())   # move front to back

        eliminated = queue.popleft()
        print(f"    {eliminated} is eliminated | Remaining: {list(queue)}")

    return queue[0]

players = ["Trush", "Rahul", "Charlie", "Diana", "Eve"]
print(f"  Players: {players}")
winner = hot_potato(players, 3)
print(f"  Winner: {winner}")
print()

# =============================
# 7. BFS PREVIEW (QUEUE APPLICATION)
# =============================

print("=== BFS Preview — Level Order Processing ===")
print()

# Simple tree as nested dict
tree = {
    "CEO": {
        "CTO": {
            "Dev Lead": {"Dev 1": {}, "Dev 2": {}},
            "QA Lead": {"QA 1": {}},
        },
        "CFO": {
            "Accountant": {},
        },
    }
}

def bfs_print(tree):
    """Print tree level by level using a queue."""
    queue = deque()
    # Start with root entries
    for name, children in tree.items():
        queue.append((name, 0, children))

    current_level = -1
    while queue:
        name, level, children = queue.popleft()

        if level != current_level:
            current_level = level
            print(f"  Level {level}:")

        print(f"    {name}")

        for child_name, grandchildren in children.items():
            queue.append((child_name, level + 1, grandchildren))

print("  Organization chart (BFS):")
bfs_print(tree)
print()
print("  → BFS uses a queue to process level by level")
print("  → We'll cover BFS in detail with graphs")
print()

# =============================
# 8. RECENT REQUESTS COUNTER
# =============================

print("=== Recent Requests Counter ===")
print()

class RecentCounter:
    """Count requests within a time window."""

    def __init__(self, window_ms=3000):
        self._requests = deque()
        self._window = window_ms

    def ping(self, timestamp):
        """Record a request and return count within window."""
        self._requests.append(timestamp)
        # Remove requests outside the window
        while self._requests[0] < timestamp - self._window:
            self._requests.popleft()
        return len(self._requests)

counter = RecentCounter(window_ms=3000)
timestamps = [1, 100, 3001, 3002, 5000, 6000, 7000]

for t in timestamps:
    count = counter.ping(t)
    print(f"  Time {t:>5}: {count} requests in window")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Implement a queue using two stacks
# 2. Implement a circular buffer of fixed size
# 3. Build a print queue that processes documents
#    in FIFO order, showing the document being printed
# ============================================
