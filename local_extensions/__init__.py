from cookiecutter.utils import simple_filter


@simple_filter
def package_name(v) -> str:
    """Return the package name (without namespace)."""
    return v.split(".")[1]


@simple_filter
def package_namespace(v) -> str:
    """Return the package namespace."""
    return v.split(".")[0]
