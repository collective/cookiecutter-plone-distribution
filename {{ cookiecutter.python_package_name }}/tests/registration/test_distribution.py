from pathlib import Path
from plone.distribution.api import distribution as dist_api
from plone.distribution.core import Distribution

import pytest


DISTRIBUTION_NAME = "{{ cookiecutter.__package_name }}"


class TestDistributionRegistration:
    distribution: Distribution = None

    @pytest.fixture(autouse=True)
    def _dist_intranet_volto(self, integration) -> Distribution:
        self.distribution = dist_api.get(name=DISTRIBUTION_NAME)

    def test_distribution_class(self):
        distribution = self.distribution
        assert isinstance(distribution, Distribution)

    @pytest.mark.parametrize(
        "attr,expected",
        [
            ["title", "{{ cookiecutter.distribution_title }}"],
            [
                "description",
                "{{ cookiecutter.description }}",
            ],
        ],
    )
    def test_distribution_name_description(self, attr, expected):
        distribution = self.distribution
        assert isinstance(distribution, Distribution)
        assert getattr(distribution, attr, expected)

    def test_distribution_has_pre_handler(self):
        distribution = self.distribution
        assert distribution.pre_handler is not None

    def test_distribution_has_no_handler(self):
        distribution = self.distribution
        assert distribution.handler is None

    def test_distribution_has_post_handler(self):
        distribution = self.distribution
        assert distribution.post_handler is not None

    @pytest.mark.parametrize(
        "profile",
        [
            "plone.app.contenttypes:default",
            "plone.app.caching:default",
            "plonetheme.barceloneta:default",
            {%- if cookiecutter.include_features == '1' %}
            "{{ cookiecutter.python_package_name }}:default",
            {%- endif %}
        ],
    )
    def test_distribution_profiles(self, profile):
        distribution = self.distribution
        assert profile in distribution.profiles

    def test_distribution_has_image(self):
        distribution = self.distribution
        assert isinstance(distribution.image, Path)
        assert distribution.image.exists()

    def test_distribution_has_local_directory(self):
        distribution = self.distribution
        assert isinstance(distribution.directory, Path)
        assert distribution.directory.exists()

    def test_distribution_has_contents_folder(self):
        distribution = self.distribution
        contents_folder = distribution.contents["json"]
        assert isinstance(contents_folder, Path)
        assert contents_folder.exists()
