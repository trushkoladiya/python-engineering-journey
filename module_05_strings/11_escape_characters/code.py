# ============================================
# MODULE 5 - SUBTOPIC 11: Escape Characters
# ============================================

# =============================
# 1. NEW LINE (\n)
# =============================

# --- Example 1: Basic newline ---
print("Hello\nWorld")
# Hello
# World

# --- Example 2: Multiple newlines ---
print("Line 1\nLine 2\nLine 3")

# --- Example 3: Newline in a variable ---
greeting = "Good\nMorning"
print()
print(greeting)

# =============================
# 2. TAB (\t)
# =============================

# --- Example 4: Basic tab ---
print()
print("Name\tAge\tCity")
print("Trush\t21\tAhmedabad")
print("Rahul\t22\tMumbai")

# --- Example 5: Tab-formatted output ---
print()
print("Item\t\tPrice")
print("----\t\t-----")
print("Apple\t\t$1.50")
print("Banana\t\t$0.75")
print("Cherry\t\t$3.00")

# =============================
# 3. BACKSLASH (\\)
# =============================

# --- Example 6: File paths ---
print()
print("Windows path: C:\\Users\\Trush\\Documents")
print("Another path: C:\\Program Files\\Python")

# --- Example 7: Literal backslash ---
print("Backslash: \\")
print("Two backslashes: \\\\")

# =============================
# 4. QUOTES (\' and \")
# =============================

# --- Example 8: Double quotes inside double-quoted string ---
print()
print("She said \"Hello\" to everyone.")
print("The file is called \"data.txt\".")

# --- Example 9: Single quote inside single-quoted string ---
print('It\'s a beautiful day.')
print('Don\'t worry, be happy!')

# --- Example 10: Mix — no escaping needed ---
print("It's easy with double quotes")     # no escape needed
print('She said "Hello" easily')           # no escape needed

# =============================
# 5. COMBINING ESCAPE CHARACTERS
# =============================

# --- Example 11: Multiple escape types ---
print()
print("Report:\n\tName:\tTrush\n\tAge:\t21\n\tCity:\tAhmedabad")

# --- Example 12: Building a formatted display ---
print()
print("=" * 30)
print("\\t = Tab character")
print("\\n = Newline character")
print("\\\\ = Backslash character")
print("\\\" = Double quote character")
print("\\' = Single quote character")
print("=" * 30)

# =============================
# 6. RAW STRINGS
# =============================

# --- Example 13: Raw strings ignore escapes ---
print()
print("Normal:", "Hello\nWorld")   # newline is processed
print("Raw:", r"Hello\nWorld")     # \n is printed literally

# --- Example 14: File paths with raw strings ---
# Without raw string — need double backslashes:
path1 = "C:\\Users\\Trush\\new_folder"
# With raw string — much cleaner:
path2 = r"C:\Users\Trush\new_folder"
print()
print("Escaped:", path1)
print("Raw:    ", path2)
print("Same?", path1 == path2)   # True!

# --- Example 15: Raw strings are useful for patterns ---
print()
print(r"\n means newline")
print(r"\t means tab")
print(r"\\ means backslash")

# =============================
# 7. SPECIAL CASES
# =============================

# --- Example 16: Newline at the end ---
print()
print("No extra line", end="")
print(" — same line!")

# --- Example 17: Using end parameter ---
print()
for i in range(5):
    print(i, end=" ")
print()   # final newline

# --- Example 18: Escape characters in variables ---
tab = "\t"
newline = "\n"
text = "Hello" + tab + "World" + newline + "Python" + tab + "Programming"
print()
print(text)

# --- Example 19: repr() shows escape characters ---
text = "Hello\tWorld\n"
print()
print("Normal print:", text)
print("repr() print:", repr(text))   # 'Hello\tWorld\n'

# ============================================
# TRY IT YOURSELF:
# 1. Print a file path like: C:\Users\You\Desktop using escaped backslashes
# 2. Print the same path using a raw string
# 3. Create a tabular display of 3 students with Name, Age, Grade using \t
# ============================================
