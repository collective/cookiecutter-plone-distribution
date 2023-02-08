"""Pytest configuration."""

import pytest


@pytest.fixture(scope="session")
def context() -> dict:
    """Cookiecutter context."""
    return {
        "distribution_title": "Blog",
        "description": "A Tech blog.",
        "github_organization": "plonegovbr",
        "python_package_name": "ploneorgbr.blog",
        "author": "PloneGov-BR",
        "email": "gov@plone.org.br",
    }


@pytest.fixture(scope="session")
def bad_context() -> dict:
    """Cookiecutter context with invalid data."""
    return {
        "distribution_title": "Blog",
        "description": "A Tech blog.",
        "github_organization": "plonegovbr",
        "python_package_name": "ploneorgbr_blog",
        "author": "PloneGov-BR",
        "email": "gov@plone.org.br",
    }


@pytest.fixture(scope="session")
def cutter_result(cookies_session, context):
    """Cookiecutter result."""
    return cookies_session.bake(extra_context=context)
