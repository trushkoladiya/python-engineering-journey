# ============================================
# MODULE 13 - SUBTOPIC 10: Composition vs Inheritance
# ============================================

# Inheritance = "is-a"  (Dog IS an Animal)
# Composition = "has-a" (Car HAS an Engine)
# When in doubt, prefer composition.

# =============================
# 1. INHERITANCE GONE WRONG
# =============================

# --- Example 1: Deep inheritance = fragile code ---
print("=== Inheritance Gone Wrong ===")
print()

# BAD: Too many levels
class BaseWidget:
    def render(self):
        return "BaseWidget"

class StyledWidget(BaseWidget):
    def render(self):
        return f"Styled({super().render()})"

class BorderedWidget(StyledWidget):
    def render(self):
        return f"Bordered({super().render()})"

class ShadowedWidget(BorderedWidget):
    def render(self):
        return f"Shadowed({super().render()})"

w = ShadowedWidget()
print(f"  Deep inheritance: {w.render()}")
print("  Problem: changing BaseWidget breaks everything!")
print("  Problem: can't mix-and-match (shadow without border?)")
print()

# =============================
# 2. COMPOSITION FIX
# =============================

# --- Example 2: Same features, using composition ---
print("=== Composition Fix ===")
print()

class Widget:
    def __init__(self, content="Widget"):
        self.content = content
        self.decorators = []

    def add_decorator(self, decorator):
        self.decorators.append(decorator)
        return self    # allows chaining

    def render(self):
        result = self.content
        for decorator in self.decorators:
            result = decorator.apply(result)
        return result

class StyleDecorator:
    def apply(self, content):
        return f"Styled({content})"

class BorderDecorator:
    def apply(self, content):
        return f"Bordered({content})"

class ShadowDecorator:
    def apply(self, content):
        return f"Shadowed({content})"

# Mix and match freely!
w1 = Widget("Button")
w1.add_decorator(StyleDecorator())
w1.add_decorator(BorderDecorator())
print(f"  Styled + Border: {w1.render()}")

w2 = Widget("Input")
w2.add_decorator(ShadowDecorator())
print(f"  Shadow only: {w2.render()}")

w3 = Widget("Card")
w3.add_decorator(BorderDecorator())
w3.add_decorator(ShadowDecorator())
w3.add_decorator(StyleDecorator())
print(f"  All three: {w3.render()}")
print()

# =============================
# 3. REAL EXAMPLE: NOTIFICATION SYSTEM
# =============================

# --- Example 3: Inheritance approach (rigid) ---
print("=== Notification: Inheritance (Rigid) ===")
print()

class Notifier:
    def send(self, msg):
        return f"Base: {msg}"

class EmailNotifier(Notifier):
    def send(self, msg):
        return f"Email: {msg}"

class SMSNotifier(Notifier):
    def send(self, msg):
        return f"SMS: {msg}"

# What if you need Email + SMS? Create ANOTHER class?
# class EmailAndSMSNotifier(EmailNotifier, SMSNotifier): ???
# This gets messy fast!

print("  Email: " + EmailNotifier().send("Hello"))
print("  SMS: " + SMSNotifier().send("Hello"))
print("  Email+SMS? Need a new class for every combo!")
print()

# --- Example 4: Composition approach (flexible) ---
print("=== Notification: Composition (Flexible) ===")
print()

class EmailChannel:
    def send(self, msg):
        return f"Email: {msg}"

class SMSChannel:
    def send(self, msg):
        return f"SMS: {msg}"

class SlackChannel:
    def send(self, msg):
        return f"Slack: {msg}"

class NotificationService:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)

    def notify(self, msg):
        results = []
        for channel in self.channels:
            results.append(channel.send(msg))
        return results

# Mix and match — no new classes needed!
service = NotificationService()
service.add_channel(EmailChannel())
service.add_channel(SMSChannel())
service.add_channel(SlackChannel())

results = service.notify("Server is down!")
for r in results:
    print(f"  {r}")
print()

# =============================
# 4. WHEN TO USE INHERITANCE
# =============================

# --- Example 5: Legitimate inheritance ---
print("=== When Inheritance IS Right ===")
print()

# GOOD: True "is-a" with shared interface
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for s in shapes:
    print(f"  {s.name}: area = {s.area():.2f}")
print("  → True 'is-a': Circle IS a Shape. Shallow hierarchy.")
print()

# =============================
# 5. SWAPPING PARTS WITH COMPOSITION
# =============================

# --- Example 6: Easy to change behavior ---
print("=== Swapping Parts ===")
print()

class ConsoleLogger:
    def log(self, msg):
        print(f"    [Console] {msg}")

class FileLogger:
    def log(self, msg):
        print(f"    [File] {msg}")

class SilentLogger:
    def log(self, msg):
        pass    # do nothing

class Application:
    def __init__(self, logger):
        self.logger = logger     # INJECTED via composition

    def run(self):
        self.logger.log("App started")
        self.logger.log("Processing...")
        self.logger.log("Done")

print("  With ConsoleLogger:")
app1 = Application(ConsoleLogger())
app1.run()
print()

print("  With FileLogger:")
app2 = Application(FileLogger())
app2.run()
print()

print("  With SilentLogger:")
app3 = Application(SilentLogger())
app3.run()
print("  (no output — logger does nothing)")
print()

# =============================
# 6. DECISION GUIDE
# =============================

print("=== When to Use What ===")
print()
print("  Use INHERITANCE when:")
print("    ✓ True 'is-a' relationship")
print("    ✓ Shared interface + behavior")
print("    ✓ Hierarchy is shallow (1-2 levels)")
print()
print("  Use COMPOSITION when:")
print("    ✓ 'Has-a' relationship")
print("    ✓ Need to mix behaviors flexibly")
print("    ✓ Parts should be swappable")
print("    ✓ You're unsure → default to composition")

# ============================================
# TRY IT YOURSELF:
# 1. Refactor a deep inheritance chain to use composition
# 2. Create a system where you can swap components at runtime
# 3. Build a class that combines 3 different behaviors via composition
# ============================================
