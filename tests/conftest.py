"""Pytest configuration."""
import re
from copy import deepcopy
from pathlib import Path
from typing import List

import pytest

ROOT_FILES = [
    ".dockerignore",
    ".editorconfig",
    ".github/workflows/meta.yml",
    ".gitignore",
    ".meta.toml",
    ".pre-commit-config.yaml",
    "CHANGES.md",
    "constraints.txt",
    "CONTRIBUTORS.md",
    "Dockerfile",
    "instance.yaml",
    "LICENSE.GPL",
    "LICENSE.md",
    "Makefile",
    "MANIFEST.in",
    "mx.ini",
    "pyproject.toml",
    "README.md",
    "requirements-docker.txt",
    "requirements.txt",
    "setup.py",
    "tox.ini",
]


PKG_SRC_FILES = [
    "__init__.py",
    "distributions/{package_name}/content/content.json",
    "distributions/{package_name}/content/ordering.json",
    "distributions/{package_name}/content/portal.json",
    "distributions/{package_name}/image.png",
    "distributions/{package_name}/profiles.json",
    "distributions/{package_name}/schema.json_example",
    "configure.zcml",
    "dependencies.zcml",
    "distributions.zcml",
    "handlers.py",
    "testing.py",
]


PKG_SRC_FEATURE_FILES = [
    "controlpanel/__init__.py",
    "controlpanel/configure.zcml",
    "indexers/__init__.py",
    "indexers/configure.zcml",
    "profiles/default/browserlayer.xml",
    "profiles/default/catalog.xml",
    "profiles/default/controlpanel.xml",
    "profiles/default/diff_tool.xml",
    "profiles/default/metadata.xml",
    "profiles/default/registry/plone.base.interfaces.controlpanel.IMailSchema.xml",  # noQA
    "profiles/default/registry/plone.base.interfaces.controlpanel.ISiteSchema.xml",  # noQA
    "profiles/default/repositorytool.xml",
    "profiles/default/rolemap.xml",
    "profiles/default/theme.xml",
    "profiles/default/types.xml",
    "profiles/default/types/.gitkeep",
    "profiles/uninstall/browserlayer.xml",
    "setuphandlers/__init__.py",
    "upgrades/__init__.py",
    "upgrades/configure.zcml",
    "vocabularies/__init__.py",
    "vocabularies/configure.zcml",
]


@pytest.fixture(scope="session")
def variable_pattern():
    return re.compile("{{( ?cookiecutter)[.](.*?)}}")


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
        "include_features": "0",
    }


@pytest.fixture(scope="session")
def context_features(context) -> dict:
    """Cookiecutter context with features enabled."""
    new_context = deepcopy(context)
    new_context["python_package_name"] = "ploneorgbr.blogredux"
    new_context["include_features"] = "1"
    return new_context


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


@pytest.fixture
def build_files_list():
    def func(root_dir: Path) -> List[Path]:
        """Build a list containing absolute paths to the generated files."""
        return [path for path in Path(root_dir).glob("*") if path.is_file()]

    return func


@pytest.fixture(scope="session")
def cutter_result(cookies_session, context):
    """Cookiecutter result."""
    return cookies_session.bake(extra_context=context)
