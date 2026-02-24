# AGENTS.md - Keeper Training Development Guide

## Project Overview

- **Type**: Django web application (Cookiecutter Django template)
- **Purpose**: Plan and manage goalkeeper training sessions
- **Python**: 3.13 | **Django**: 3.2+

## Tech Stack

- Django 3.2+ with Django REST Framework
- PostgreSQL 18, pytest, factory-boy, uv

---

## Running the Application

```bash
# Build and run the stack
docker compose -f docker-compose.local.yml up

# Rebuild (after adding dependencies)
docker compose -f docker-compose.local.yml up -d --build

# Run management commands
docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
docker compose -f docker-compose.local.yml run --rm django python manage.py shell

# Run tests inside container
docker compose -f docker-compose.local.yml run --rm django pytest
docker compose -f docker-compose.local.yml run --rm django pytest keeper_training/users/tests/test_models.py::test_user_get_absolute_url
```

---

## Testing

```bash
# Run all tests
docker compose -f docker-compose.local.yml run --rm django pytest

# Run a single test file
docker compose -f docker-compose.local.yml run --rm django pytest keeper_training/users/tests/test_models.py

# Run a specific test
docker compose -f docker-compose.local.yml run --rm django pytest keeper_training/users/tests/test_models.py::test_user_get_absolute_url

# Run tests matching a pattern
docker compose -f docker-compose.local.yml run --rm django pytest -k "test_user"

# Run with coverage
docker compose -f docker-compose.local.yml run --rm django coverage run -m pytest
docker compose -f docker-compose.local.yml run --rm django coverage html
```

---

## Linting & Code Quality

```bash
# Run all linters (pre-commit)
pre-commit run --all-files

# Individual linters
ruff check keeper_training/
ruff format keeper_training/
mypy keeper_training
```

---

## Code Style Guidelines

### General

- **Line Length**: 120 characters max
- **Formatting**: Ruff
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

Hooks: trailing-whitespace, end-of-file-fixer, check-yaml, reorder-python-imports, ruff

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
