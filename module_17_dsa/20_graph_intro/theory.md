# Graphs (Intro)

## What Is a Graph?

A **graph** is a collection of **nodes** (vertices) connected by **edges**. Unlike trees, graphs can have cycles and any node can connect to any other.

```
    A --- B
    |     |
    C --- D --- E
```

## Terminology

| Term | Meaning |
|------|---------|
| Vertex (Node) | A point in the graph |
| Edge | A connection between two vertices |
| Directed | Edges have a direction (A → B) |
| Undirected | Edges go both ways (A — B) |
| Path | A sequence of connected vertices |
| Cycle | A path that returns to the starting vertex |

## Representation: Adjacency List

The most common way to represent a graph in Python — a dictionary where each key is a node and the value is a list of neighbors:

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}
```

## Traversals

### DFS (Depth-First Search)
Go as deep as possible before backtracking. Uses a **stack** (or recursion).

### BFS (Breadth-First Search)
Visit all neighbors first, then their neighbors. Uses a **queue**.

## Key Points

- Graphs model relationships: social networks, maps, dependencies
- Adjacency list is the standard Python representation
- DFS → uses stack/recursion, explores deeply
- BFS → uses queue, explores level by level
- Both are O(V + E) where V = vertices, E = edges
