# ============================================
# MODULE 17 - SUBTOPIC 20: Graphs (Intro)
# ============================================

# Graphs: nodes connected by edges.
# Representation: adjacency list (dict of lists).
# Traversal: DFS (stack) and BFS (queue).

from collections import deque

# =============================
# 1. GRAPH REPRESENTATION
# =============================

print("=== Graph Representation — Adjacency List ===")
print()

# Undirected graph:
#     A --- B
#     |     |
#     C --- D --- E

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

print("  Graph (adjacency list):")
for node, neighbors in graph.items():
    print(f"    {node} → {neighbors}")
print()

# =============================
# 2. DFS — DEPTH-FIRST SEARCH (RECURSIVE)
# =============================

print("=== DFS — Recursive ===")
print()

def dfs_recursive(graph, node, visited=None):
    """Depth-first search using recursion."""
    if visited is None:
        visited = set()

    visited.add(node)
    print(f"    Visiting: {node}")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited

print("  DFS from A:")
visited = dfs_recursive(graph, "A")
print(f"  Visited: {visited}")
print()

# =============================
# 3. DFS — ITERATIVE (USING STACK)
# =============================

print("=== DFS — Iterative (Stack) ===")
print()

def dfs_iterative(graph, start):
    """Depth-first search using a stack."""
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Add neighbors in reverse for consistent order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order

order = dfs_iterative(graph, "A")
print(f"  DFS order from A: {order}")
print()

# =============================
# 4. BFS — BREADTH-FIRST SEARCH
# =============================

print("=== BFS — Breadth-First Search ===")
print()

def bfs(graph, start):
    """Breadth-first search using a queue."""
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        print(f"    Visiting: {node} (neighbors: {graph[node]})")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

print("  BFS from A:")
order = bfs(graph, "A")
print(f"  BFS order: {order}")
print()

# =============================
# 5. DFS vs BFS COMPARISON
# =============================

print("=== DFS vs BFS Comparison ===")
print()

# Larger graph
city_graph = {
    "New York": ["Boston", "Philadelphia"],
    "Boston": ["New York", "Portland"],
    "Philadelphia": ["New York", "Baltimore"],
    "Portland": ["Boston"],
    "Baltimore": ["Philadelphia", "Washington"],
    "Washington": ["Baltimore"],
}

print("  City connections:")
for city, connections in city_graph.items():
    print(f"    {city} ↔ {', '.join(connections)}")
print()

dfs_order = dfs_iterative(city_graph, "New York")
bfs_order = bfs(city_graph, "New York")
print(f"  DFS from New York: {dfs_order}")
print(f"  BFS from New York: {bfs_order}")
print()

# =============================
# 6. FIND PATH BETWEEN NODES
# =============================

print("=== Find Path Between Nodes ===")
print()

def find_path_dfs(graph, start, end, path=None):
    """Find a path from start to end using DFS."""
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            result = find_path_dfs(graph, neighbor, end, path)
            if result:
                return result
    return None

path = find_path_dfs(graph, "A", "E")
print(f"  Path A → E: {' → '.join(path)}")

path = find_path_dfs(city_graph, "Portland", "Washington")
print(f"  Path Portland → Washington: {' → '.join(path)}")
print()

# =============================
# 7. SHORTEST PATH (BFS)
# =============================

print("=== Shortest Path (BFS) ===")
print()

def shortest_path(graph, start, end):
    """Find shortest path using BFS."""
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

path = shortest_path(city_graph, "Portland", "Washington")
print(f"  Shortest Portland → Washington: {' → '.join(path)}")
print(f"  Length: {len(path) - 1} edges")
print()

# =============================
# 8. DETECT CYCLE
# =============================

print("=== Detect Cycle in Graph ===")
print()

def has_cycle(graph):
    """Detect cycle in undirected graph."""
    visited = set()

    def dfs_cycle(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_cycle(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs_cycle(node, None):
                return True
    return False

print(f"  Graph has cycle: {has_cycle(graph)}")

# Graph without cycle (tree)
tree_graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A", "D"],
    "D": ["C"],
}
print(f"  Tree (no cycle): {has_cycle(tree_graph)}")
print()

# =============================
# 9. CONNECTED COMPONENTS
# =============================

print("=== Connected Components ===")
print()

def find_components(graph):
    """Find all connected components."""
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            components.append(component)

    return components

# Disconnected graph
disconnected = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D"],
    "D": ["C", "E"],
    "E": ["D"],
    "F": [],
}

components = find_components(disconnected)
print(f"  Graph nodes: {list(disconnected.keys())}")
print(f"  Components: {components}")
print(f"  Number of components: {len(components)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Build a directed graph and implement DFS/BFS on it
# 2. Find ALL paths between two nodes (not just one)
# 3. Check if a graph is bipartite (two-colorable)
# ============================================
