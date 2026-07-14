# Object Relationships: Association, Aggregation, Composition

Objects don't exist in isolation — they **relate** to each other. There are three main types of relationships.

## Association (Loosest)

Two objects are **connected** but **independent**. Neither owns the other.

```python
class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

# Teacher and Student are associated — connected but independent
teacher = Teacher("Mr. Smith")
student = Student("Trush")
```

Think: A teacher **knows** a student, but neither depends on the other to exist.

## Aggregation (Weak Ownership)

One object **has** another, but the contained object can **exist independently**.

```python
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

# Employee exists independently — department just references it
emp = Employee("Trush")
dept = Department("Engineering")
dept.add_employee(emp)
# If dept is deleted, emp still exists
```

Think: A department **has** employees, but employees exist on their own.

## Composition (Strong Ownership)

One object **contains** another, and the contained object **cannot exist** without the container.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, hp):
        self.brand = brand
        self.engine = Engine(hp)  # created INSIDE Car

# Engine is created by Car — it doesn't exist independently
```

Think: A car **owns** its engine — the engine is part of the car.

## Summary

| Relationship | Ownership | Lifetime | Example |
|-------------|-----------|----------|---------|
| Association | None | Independent | Teacher ↔ Student |
| Aggregation | Weak | Can survive alone | Department → Employee |
| Composition | Strong | Dies with parent | Car → Engine |

## Key Points

- **Association** = objects know each other, no ownership
- **Aggregation** = "has-a" with weak ownership (parts survive)
- **Composition** = "has-a" with strong ownership (parts die with parent)
- Choose based on whether the contained object makes sense on its own
