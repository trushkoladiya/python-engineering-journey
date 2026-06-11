# Properties — `@property` Decorator

Properties let you use **methods that look like attributes**. They give you getter/setter control with clean syntax.

## The Problem

In Module 12, we used manual getters and setters:

```python
# Ugly syntax:
value = obj.get_name()
obj.set_name("Trush")
```

Properties let you write:

```python
# Clean syntax:
value = obj.name
obj.name = "Trush"
```

While still running validation code behind the scenes!

## Creating a Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):              # getter
        return self._radius

    @radius.setter
    def radius(self, value):       # setter
        if value < 0:
            raise ValueError("Radius can't be negative")
        self._radius = value

c = Circle(5)
print(c.radius)     # calls the getter → 5
c.radius = 10       # calls the setter
```

## Read-Only Properties

If you only define `@property` without a setter, the attribute is **read-only**:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.area)    # 78.54
c.area = 100     # AttributeError! No setter defined
```

## Computed Properties

Properties can **calculate** values on the fly:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
```

## Deleter

```python
@radius.deleter
def radius(self):
    print("Deleting radius")
    del self._radius
```

## Key Points

- `@property` makes methods look like attributes
- **Getter**: `@property` — runs on `obj.attr`
- **Setter**: `@attr.setter` — runs on `obj.attr = value`
- **Deleter**: `@attr.deleter` — runs on `del obj.attr`
- Read-only properties: define getter without setter
- Computed properties: calculate values dynamically
