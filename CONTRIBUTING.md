# Contributing to DeliberativePolling

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Development Setup

### 1. Fork and Clone

```bash
# Clone the repository
git clone https://github.com/stanford-ddl/DeliberativePolling.git
cd DeliberativePolling
```

### 2. Set Up Environment

```bash
# Create a virtual environment
python3 -m venv env

# Activate it
source env/bin/activate  # macOS/Linux
# env\Scripts\activate   # Windows

# Install in editable mode
pip install -e .
```

### 3. Verify Installation

```python
from DeliberativePolling import outputs
outputs("Sample.sav", fast=True)
```

---

## Making Changes

### Workflow

1. **Create a branch** from `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b fix/your-feature-name
   ```

2. **Make your changes** - Edit files in `DeliberativePolling/`

3. **Test locally** - Run the package on sample data to verify changes work

4. **Commit** with a clear message:
   ```bash
   git add .
   git commit -m "Fix: Brief description of change
   
   - More detailed explanation
   - Why the change was needed
   - How it solves the problem"
   ```

5. **Push** your branch:
   ```bash
   git push origin fix/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

---

## Branch Naming

Use these prefixes:

- `fix/` - Bug fixes (e.g., `fix/nominal-crosstab-nan`)
- `feature/` - New features (e.g., `feature/db-export`)
- `refactor/` - Code restructuring
- `docs/` - Documentation updates
- `test/` - Adding or updating tests

---

## Commit Messages

### Format

```
Type: Brief summary (50 chars or less)

Detailed explanation of the change (wrap at 72 chars):
- What the problem was
- How this change addresses it
- Any side effects or considerations
```

### Types

- `Fix:` - Bug fixes
- `Feature:` - New features
- `Refactor:` - Code restructuring
- `Docs:` - Documentation
- `Test:` - Tests
- `Chore:` - Maintenance

### Examples

Good:
```
Fix: Handle NaN values in nominal crosstabs

- Problem: Crosstabs would fail when nominal categories existed 
  in one wave but were all NaN in another wave
- Solution: Use all labels from SPSS metadata rather than just
  values present in data
- Ensures consistent table structure across waves
```

Not as good:
```
Update __init__.py
```

---

## Code Style

- Follow PEP 8 guidelines
- Use descriptive variable names
- Add comments for complex logic
- Keep functions focused on single responsibilities

---

## Testing

Before submitting a PR:

1. Test on `Sample.sav` to verify basic functionality
2. Test on your own data if possible
3. Check that outputs are generated correctly
4. Verify no errors in different scenarios (missing data, multiple waves, etc.)

---

## Project Structure

```
DeliberativePolling/
├── DeliberativePolling/     # Main package code
│   └── __init__.py             # All package functions
├── setup.py                    # Package configuration
├── README.md                   # User-facing documentation
├── CONTRIBUTING.md             # This file
├── Sample.sav                  # Example SPSS data
└── Images/                     # Documentation images
```

---

## Key Functions in `__init__.py`

### Main Entry Point
- `outputs()` - Primary function that orchestrates the entire analysis

### Data Processing
- `subsample` - Class for managing subsets of data by group/wave
- `crosstab_create()` - Generates crosstabs for nominal or ordinal variables
- `crosstab_means()` - Calculates means and adds them to crosstabs
- `ordinal_crosstab()` - Handles ordinal variable analysis
- `nominal_crosstab()` - Handles nominal variable analysis

### Statistical Tests
- `t_test()` - Performs t-tests for ordinal variable comparisons
- `x_test()` - Performs chi-square tests for nominal variables

### Output Generation
- `write_xlsx()` - Generates Excel files
- `write_docx()` - Generates Word documents
- `document_title()` - Creates file names
- `comparison_name()` - Creates comparison labels

### Utilities
- `check_labels()` - Validates SPSS metadata
- `check_numeric()` - Ensures variables are numeric type
- `plurality()` - Finds most common response
- `add_sample_size()` - Adds sample size to labels

---

## Common Development Tasks

### Adding a New Feature

1. Understand the current code flow by tracing `outputs()` function
2. Identify where your feature fits in the pipeline
3. Create helper functions if needed
4. Update relevant sections in README.md
5. Test thoroughly

### Fixing a Bug

1. Reproduce the bug with minimal example
2. Identify the root cause (often in crosstab functions)
3. Fix and add comments explaining the solution
4. Test with various edge cases
5. Update troubleshooting section in README if needed

### Improving Performance

Focus on these high-impact areas:
- `write_docx()` - Word generation is slow
- `crosstab_create()` - Called many times
- Loops over nominal/ordinal variables

---

## Pull Request Guidelines

### Before Submitting

- [ ] Code works locally
- [ ] Tested on `Sample.sav`
- [ ] No new errors or warnings
- [ ] Commit messages are clear
- [ ] README updated if needed

### PR Description Template

```markdown
## Summary
Brief description of changes

## Problem
What issue does this address?

## Solution
How does this PR solve it?

## Testing
What testing was done?

## Breaking Changes
Any backward-incompatible changes?
```

---

## Release Process

(For maintainers)

1. Update version in `setup.py`
2. Update README with changes
3. Create git tag: `git tag v1.4.3`
4. Push tag: `git push origin v1.4.3`
5. Build and upload to PyPI:
   ```bash
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```

---

## Questions?

- Open a [GitHub issue](https://github.com/stanford-ddl/DeliberativePolling/issues)
- Email: deliberation@stanford.edu
