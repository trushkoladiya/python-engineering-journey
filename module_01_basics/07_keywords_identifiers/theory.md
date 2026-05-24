# Keywords & Identifiers

## 1. Keywords (Reserved Words)

Keywords are **special words** that Python uses for its own rules. You **cannot** use them as variable names.

### Common Python Keywords

```
False    True     None
and      or       not
if       else     elif
for      while    break
continue pass     return
def      class    import
from     as       in
is       with     try
except   finally  raise
```

Example — this will **cause an error**:

```python
# if = 10  ❌ Error — "if" is a keyword
```

## 2. Identifiers

An identifier is any **name** you create — variable names, etc.

### Rules for Identifiers

| Rule | Valid | Invalid |
|------|-------|---------|
| Letters, digits, underscore | `my_var`, `age2` | — |
| Must start with letter or `_` | `_count`, `name` | `2name` |
| No spaces | `user_name` | `user name` |
| No special characters | `score` | `my-var`, `my@var` |
| Case sensitive | `age` ≠ `Age` | — |

### Naming Conventions

```python
user_name = "Trush"    # ✅ snake_case (recommended for variables)
userName = "Trush"     # ⚠️ works but not Pythonic
UserName = "Trush"     # ⚠️ usually for classes (later modules)
```

## Key Points

- Keywords are reserved — don't use them as names
- Identifiers must start with a letter or `_`
- Use `snake_case` for variable names
- Names are case-sensitive
