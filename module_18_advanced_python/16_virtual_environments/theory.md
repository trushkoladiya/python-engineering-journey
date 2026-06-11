# Virtual Environments & Dependency Management

## Why Virtual Environments?

Different projects need different package versions. Without isolation:
- Project A needs `requests==2.25` 
- Project B needs `requests==2.31`
- They'd conflict if installed globally!

A **virtual environment** creates an **isolated** Python installation for each project.

## Creating a Virtual Environment

```bash
# Create a virtual environment
python3 -m venv myproject_env

# Activate it
source myproject_env/bin/activate    # Linux/Mac
myproject_env\Scripts\activate       # Windows

# Deactivate when done
deactivate
```

When activated, `pip install` puts packages in the virtual environment, not globally.

## Managing Dependencies

```bash
# Install packages
pip install requests flask

# See installed packages
pip list

# Save dependencies to a file
pip freeze > requirements.txt

# Install from requirements file (on another machine)
pip install -r requirements.txt
```

## requirements.txt Format

```
requests==2.31.0
flask==3.0.0
numpy>=1.24.0
pandas~=2.0.0
```

| Syntax | Meaning |
|--------|---------|
| `==2.31.0` | Exact version |
| `>=1.24.0` | Minimum version |
| `~=2.0.0` | Compatible release (2.0.x) |
| `<=3.0` | Maximum version |

## Best Practices

1. **Always** use a virtual environment for each project
2. **Never** install project packages globally
3. **Always** maintain a `requirements.txt`
4. Add `venv/` or `env/` to `.gitignore`
5. Use clear, descriptive environment names

## Key Points

- `python3 -m venv <name>` creates a virtual environment
- Activate with `source <name>/bin/activate`
- `pip freeze > requirements.txt` saves dependencies
- `pip install -r requirements.txt` restores them
- Each project should have its own virtual environment
