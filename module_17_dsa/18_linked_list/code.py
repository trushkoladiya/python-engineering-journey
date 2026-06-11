# ============================================
# MODULE 17 - SUBTOPIC 18: Linked List
# ============================================

# Linked list: nodes connected by references.
# Each node stores data + pointer to next node.

# =============================
# 1. NODE CLASS
# =============================

print("=== Node Structure ===")
print()

class Node:
    """A single node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

# Create individual nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link them together
node1.next = node2
node2.next = node3

# Traverse manually
current = node1
while current:
    print(f"  {current.data}", end=" → " if current.next else " → None\n")
    current = current.next
print()

# =============================
# 2. LINKED LIST CLASS
# =============================

print("=== Linked List Implementation ===")
print()

class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add node at the end. O(n)."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add node at the beginning. O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete first occurrence of data."""
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        """Search for data. Returns True/False."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        """Count nodes."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        """Display list as string."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " → ".join(elements) + " → None"

    def to_list(self):
        """Convert to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Test the linked list
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.append(val)

print(f"  List: {ll.display()}")
print(f"  Length: {ll.length()}")
print(f"  Search 30: {ll.search(30)}")
print(f"  Search 99: {ll.search(99)}")
print()

# Prepend
ll.prepend(5)
print(f"  After prepend(5): {ll.display()}")

# Delete
ll.delete(30)
print(f"  After delete(30): {ll.display()}")

ll.delete(5)
print(f"  After delete(5):  {ll.display()}")
print()

# =============================
# 3. INSERT AT POSITION
# =============================

print("=== Insert at Position ===")
print()

class LinkedListExtended(LinkedList):
    """Extended linked list with more operations."""

    def insert_at(self, position, data):
        """Insert at specific position (0-indexed)."""
        if position == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def get(self, position):
        """Get data at position."""
        current = self.head
        for _ in range(position):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        return current.data if current else None

ll = LinkedListExtended()
for val in [10, 20, 30, 40]:
    ll.append(val)

print(f"  List: {ll.display()}")

ll.insert_at(2, 25)
print(f"  Insert 25 at pos 2: {ll.display()}")

ll.insert_at(0, 5)
print(f"  Insert 5 at pos 0:  {ll.display()}")

print(f"  Get pos 3: {ll.get(3)}")
print()

# =============================
# 4. REVERSE A LINKED LIST
# =============================

print("=== Reverse Linked List ===")
print()

def reverse_linked_list(ll):
    """Reverse the linked list in-place."""
    prev = None
    current = ll.head

    while current:
        next_node = current.next    # save next
        current.next = prev         # reverse pointer
        prev = current              # move prev forward
        current = next_node         # move current forward

    ll.head = prev

ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)

print(f"  Before: {ll.display()}")
reverse_linked_list(ll)
print(f"  After:  {ll.display()}")
print()

# =============================
# 5. DETECT CYCLE
# =============================

print("=== Detect Cycle (Floyd's Algorithm) ===")
print()

def has_cycle(head):
    """Detect cycle using Floyd's tortoise and hare."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # moves 1 step
        fast = fast.next.next     # moves 2 steps
        if slow == fast:
            return True
    return False

# No cycle
ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)
print(f"  {ll.display()}")
print(f"  Has cycle: {has_cycle(ll.head)}")

# Create a cycle
node = ll.head
tail = node
while tail.next:
    tail = tail.next
tail.next = node.next.next   # 5 → 3 (cycle!)
print(f"  After creating cycle (5→3): Has cycle: {has_cycle(ll.head)}")
print()

# =============================
# 6. FIND MIDDLE NODE
# =============================

print("=== Find Middle Node ===")
print()

def find_middle(head):
    """Find middle node using slow/fast pointers."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data if slow else None

ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)
print(f"  List: {ll.display()}")
print(f"  Middle: {find_middle(ll.head)}")

ll2 = LinkedList()
for val in [1, 2, 3, 4, 5, 6]:
    ll2.append(val)
print(f"  List: {ll2.display()}")
print(f"  Middle: {find_middle(ll2.head)}")
print()

# =============================
# 7. MERGE TWO SORTED LINKED LISTS
# =============================

print("=== Merge Two Sorted Linked Lists ===")
print()

def merge_sorted(head1, head2):
    """Merge two sorted linked lists."""
    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    current.next = head1 if head1 else head2

    # Build result list
    result = LinkedList()
    result.head = dummy.next
    return result

ll1 = LinkedList()
for val in [1, 3, 5, 7]:
    ll1.append(val)

ll2 = LinkedList()
for val in [2, 4, 6, 8]:
    ll2.append(val)

print(f"  List 1: {ll1.display()}")
print(f"  List 2: {ll2.display()}")

merged = merge_sorted(ll1.head, ll2.head)
print(f"  Merged: {merged.display()}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Remove duplicates from a sorted linked list
# 2. Find the nth node from the end of a linked list
# 3. Check if a linked list is a palindrome
# ============================================
