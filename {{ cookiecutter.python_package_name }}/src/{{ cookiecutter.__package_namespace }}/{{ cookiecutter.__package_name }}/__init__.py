"""Init and utils."""
import logging

from zope.i18nmessageid import MessageFactory

_ = MessageFactory("{{ cookiecutter.python_package_name }}")

logger = logging.getLogger("{{ cookiecutter.python_package_name }}")
