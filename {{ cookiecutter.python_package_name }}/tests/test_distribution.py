from plone.distribution.api import distribution as dist_api


class TestDistribution:

    def test_distribution_is_registered(self, integration):
        name = "{{ cookiecutter.__package_name }}"
        assert dist_api.get(name=name)
