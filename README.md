[![Cookiecutter Plone Project CI](https://github.com/collective/cookiecutter-plone-distribution/actions/workflows/ci.yml/badge.svg)](https://github.com/collective/cookiecutter-plone-distribution/actions/workflows/ci.yml)
[![Built with Cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter-ff69b4.svg?logo=cookiecutter)](https://github.com/collective/cookiecutter-plone-distribution/)
![GitHub](https://img.shields.io/github/license/collective/cookiecutter-plone-distribution)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Cookiecutter Plone Distribution

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), [Cookiecutter Plone Distribution](https://github.com/collective/cookiecutter-plone-distribution/) is intended to be used by Plone integrations willing to implement their own Plone Distributions.

A Plone distribution is a pre-packaged version of Plone that includes specific features, themes, modules, and configurations. It is a convenient way to get a specific type of website up and running quickly, as the distribution includes everything needed to run that type of site.


## Features

- For Plone 6
- Works with Python 3.8, 3.9, 3.10, 3.11


## Requirements

### Cookiecutter

Install `cookiecutter` command line:

```shell
pip install cookiecutter
```

## Usage

Generate a new Plone Distribution package:

```shell
cookiecutter gh:collective/cookiecutter-plone-distribution
```

`Cookiecutter` generates a file structure.


## Project Generation Options

These are all the template options that will be prompted by the [Cookiecutter CLI](https://github.com/cookiecutter/cookiecutter) before generating your project.

| Option                | Description                                                                                                                                          | Example                       |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `distribution_title`       | Your project's human-readable name, capitals and spaces allowed.                                                                                     | **Blog**                |
| `description`         | Describes your project and gets used in places like ``README.md`` and such.                                                                          | **Create awesome blogs with Plone.** |
| `github_organization` | Used for GitHub and Docker repositories.                                                                                                             | **collective**                |
| `python_package_name`        | Name of the Python package used to configure your project. It needs to be Python-importable, so no dashes, spaces or special characters are allowed. | **collective.blog**    |
| `author`              | This is you! The value goes into places like ``LICENSE``, ``setup.py`` and such.                                                                     | **Our Company**               |
| `email`               | The email address you want to identify yourself in the project.                                                                                      | **email@example.com**         |


## Roadmap

- [ ] More tests on the generated package
- [ ] Basic documentation

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
