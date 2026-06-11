# Managing Dependencies (Intro)

Beyond Python's standard library, there's a vast ecosystem of **third-party packages** created by the community.

## What are External Packages?

Third-party packages are code written by others that you can install and use. They're hosted on **PyPI** (Python Package Index).

## Installing Packages with `pip`

`pip` is Python's package installer:

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.28.0

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests
```

## Popular Third-Party Packages

| Package | Purpose |
|---------|---------|
| `requests` | HTTP requests (web APIs) |
| `numpy` | Numerical computing |
| `pandas` | Data analysis |
| `flask` | Web framework |
| `pytest` | Testing framework |
| `pillow` | Image processing |

## `requirements.txt`

A file listing all packages a project needs:

```
requests==2.28.0
numpy>=1.23.0
pandas
```

Install all at once:
```bash
pip install -r requirements.txt
```

## Key Points

- Third-party packages extend Python's capabilities
- Use `pip install package_name` to install
- PyPI (pypi.org) hosts thousands of packages
- Use `requirements.txt` to track project dependencies
- This is just an introduction — you'll use this more as you build projects
