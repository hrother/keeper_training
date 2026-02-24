# AGENTS.md - Keeper Training Development Guide

## Project Overview

- **Type**: Django web application (Cookiecutter Django template)
- **Purpose**: Plan and manage goalkeeper training sessions
- **Python**: 3.8+ | **Django**: 3.2+

## Tech Stack

- Django 3.2+ with Django REST Framework
- PostgreSQL, pytest, factory-boy

---

## Running the Application

### Local Development (Docker)

```bash
# Build and run the stack
docker compose -f local.yml up

# Rebuild (after adding dependencies)
docker compose -f local.yml up -d --build

# Run management commands
docker compose -f local.yml run --rm django python manage.py migrate
docker compose -f local.yml run --rm django python manage.py createsuperuser
docker compose -f local.yml run --rm django python manage.py shell

# Run tests inside container
docker compose -f local.yml run --rm django pytest
docker compose -f local.yml run --rm django pytest keeper_training/users/tests/test_models.py::test_user_get_absolute_url
```

### Local Development (No Docker)

```bash
# Run development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser
```

---

## Testing

```bash
# Run all tests
pytest

# Run a single test file
pytest keeper_training/users/tests/test_models.py

# Run a specific test
pytest keeper_training/users/tests/test_models.py::test_user_get_absolute_url

# Run tests matching a pattern
pytest -k "test_user"

# Run with coverage
coverage run -m pytest
coverage html
```

---

## Linting & Code Quality

```bash
# Run all linters (pre-commit)
pre-commit run --all-files

# Individual linters
black keeper_training/
flake8 keeper_training/
mypy keeper_training
pylint keeper_training/
```

---

## Code Style Guidelines

### General

- **Line Length**: 120 characters max
- **Formatting**: Black, Import order: `reorder-python-imports`
- **Docstrings**: Google-style

### Imports

```python
import logging
from typing import Any

import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

from keeper_training.users.models import User
```

### Naming Conventions

- Models: `PascalCase` (e.g., `TrainingSession`)
- Views: `PascalCase` classes, `snake_case` functions
- Variables/Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Tests: `test_<what_is_tested>.py`, functions start with `test_`

### Django Patterns

- Use `get_user_model()` instead of importing `User` directly
- Lazy translations: `from django.utils.translation import gettext_lazy as _`
- URL patterns: `snake_case` with colons for namespacing

### Testing Patterns

- Use `pytest.mark.django_db` for database tests
- Use factory-boy for fixtures
- Test files: `tests.py` or `test_*.py`

```python
import pytest
from keeper_training.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
```

---

## Configuration

- **Settings**: `config/settings/` (base.py, local.py, production.py, test.py)
- **URLs**: `config/urls.py`
- **Test Settings**: Uses `config.settings.test`

---

## Pre-commit Hooks

Hooks: trailing-whitespace, end-of-file-fixer, check-yaml, reorder-python-imports, black, flake8

Install: `pre-commit install`

---

## Git Conventions

### Branch Naming

- Format: `gituser/short-description`
- Example: `hrother/add-user-model`

---

## Notes

- Database reused across test runs (`--reuse-db` in pytest.ini)
- MEDIA_ROOT set to tmpdir for tests (`keeper_training/conftest.py`)
- Migrations ignored by mypy and flake8
