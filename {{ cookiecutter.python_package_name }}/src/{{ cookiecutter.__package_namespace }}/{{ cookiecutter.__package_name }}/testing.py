import {{ cookiecutter.python_package_name }}  # noQA
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
{%- if cookiecutter.include_features == '1' %}
from plone.app.testing import applyProfile
{%- endif %}
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.distribution.testing.layer import PloneDistributionFixture
from plone.testing.zope import WSGI_SERVER_FIXTURE


DEFAULT_ANSWERS = {
    "site_id": "plone",
    "title": "My Site",
    "description": "Site created with {{ cookiecutter.description }}",
    "default_language": "{{ cookiecutter.default_language }}",
    "portal_timezone": "Europe/Berlin",
    "setup_content": True,
}

class BaseFixture(PloneDistributionFixture):
    PACKAGE_NAME = "{{ cookiecutter.python_package_name }}"

    SITES = (("{{ cookiecutter.__package_name }}", DEFAULT_ANSWERS),)


BASE_FIXTURE = BaseFixture()


class Layer(PloneSandboxLayer):
    defaultBases = (BASE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
{%- if cookiecutter.include_features == '1' %}
        self.loadZCML(package={{ cookiecutter.python_package_name }})

    def setUpPloneSite(self, portal):
        applyProfile(portal, "{{ cookiecutter.python_package_name }}:default")
{%- endif %}

FIXTURE = Layer()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="{{ cookiecutter.__python_package_name_upper }}Layer:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER_FIXTURE),
    name="{{ cookiecutter.__python_package_name_upper }}Layer:FunctionalTesting",
)


ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="{{ cookiecutter.__python_package_name_upper }}Layer:AcceptanceTesting",
)
