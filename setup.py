# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "mediator_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Mediator framework",
    author_email="icanlab@pub.seu.edu.cn",
    url="",
    keywords=["Swagger", "Mediator framework"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['mediator_server=mediator_server.__main__:main']},
    long_description="""\
    This is a sample Mediator server.  You can find out more about our project at [https://github.com/icanlab/mediator)
    """
)
