# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6
FROM plone/server-builder:${PLONE_VERSION} as builder

WORKDIR /app

# Add local code
COPY . src/{{ cookiecutter.python_package_name }}

# Install local requirements and pre-compile mo files
RUN <<EOT
    set -e
    mv src/{{ cookiecutter.python_package_name }}/requirements-docker.txt ./requirements.txt
    bin/pip install -r requirements.txt
    bin/python /compile_mo.py
    rm -Rf src/ /compile_mo.py compile_mo.log
EOT

FROM plone/server-prod-config:${PLONE_VERSION}

LABEL maintainer="{{ cookiecutter.author }} <{{ cookiecutter.email }}>" \
      org.label-schema.name="{{ cookiecutter.__docker_image_name }}" \
      org.label-schema.description="{{ cookiecutter.description }}" \
      org.label-schema.vendor="{{ cookiecutter.author }}"

# Disable MO Compilation
ENV zope_i18n_compile_mo_files=
# Show only our distributions
ENV ALLOWED_DISTRIBUTIONS={{ cookiecutter.__package_name }}

COPY --from=builder /app /app

RUN <<EOT
    ln -s /data /app/var
EOT
