# What is OOP (Code Perspective)

So far, you've organized code using **variables**, **functions**, and **data structures** (lists, dicts, etc.). This works well for small programs.

But as programs grow, you need a better way to **organize related data and behavior together**. That's what **Object-Oriented Programming (OOP)** does.

## The Problem Without OOP

Imagine managing student data:

```python
student1_name = "Trush"
student1_age = 21
student1_grade = "A"

student2_name = "Rahul"
student2_age = 22
student2_grade = "B"
```

With more students and operations, this becomes messy. Functions and variables are scattered everywhere.

## The OOP Idea

OOP lets you **bundle data + behavior** into a single unit called an **object**:

```python
# Instead of scattered variables...
# You create an object that holds everything together

student1.name    # "Trush"
student1.age     # 20
student1.grade   # "A"
student1.study() # behavior
```

The **data** (name, age, grade) and the **behavior** (study) live together.

## Key Concepts (Preview)

| Concept     | What It Is                          | Example                  |
|-------------|-------------------------------------|--------------------------|
| **Class**   | A blueprint/template                | `Student` blueprint      |
| **Object**  | A specific instance of a class      | `student1` (Trush)       |
| **Attribute** | Data stored in an object          | `student1.name`          |
| **Method**  | A function that belongs to an object | `student1.study()`      |

Think of it this way:
- A **class** is like a cookie cutter
- An **object** is like a cookie made from that cutter
- Each cookie (object) can have different decorations (attributes)

## Why Use OOP?

- **Organization** — related code stays together
- **Reusability** — create many objects from one blueprint
- **Clarity** — code mirrors real-world concepts

## Key Points

- OOP = organizing code by combining **data** and **behavior** into objects
- A **class** is the blueprint, an **object** is the real thing
- You already used objects! Strings, lists, dicts are all objects in Python
- OOP becomes essential as programs grow larger
