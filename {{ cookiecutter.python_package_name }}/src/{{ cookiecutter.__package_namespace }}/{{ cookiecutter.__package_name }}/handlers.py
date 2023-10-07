from plone.distribution.core import Distribution
from {{ cookiecutter.python_package_name }} import logger
from Products.CMFPlone.Portal import PloneSite


def pre_handler(answers: dict) -> dict:
    """Process answers."""
    return answers


def post_handler(
    distribution: Distribution, site: PloneSite, answers: dict
) -> PloneSite:
    """Run after site creation."""
    logger.info(f"{site.id}: Running {distribution.name} post_handler")
    return site
