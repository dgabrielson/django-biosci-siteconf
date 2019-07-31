#######################
from __future__ import print_function, unicode_literals

from biosci_siteconf import VERSION

#######################
from setuptools import find_packages, setup


def read_requirements(filename="requirements.txt"):
    return [
        line.strip()
        for line in open(filename)
        if line.strip() and line[0].strip() != "#" and not line.startswith("-e ")
    ]


setup(
    name="django-biosci-siteconf",
    version=VERSION,
    author="Dave Gabrielson",
    author_email="Dave.Gabrielson@umanitoba.ca",
    description="Biological Sciences site configuration",
    url="",
    license="",
    packages=find_packages(),
    install_requires=read_requirements(),
    zip_safe=False,
    include_package_data=True,
    scripts=["scripts/manage.py"],
)
