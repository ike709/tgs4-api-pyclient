# coding: utf-8

"""
    TGS API

    A production scale tool for BYOND server management  # noqa: E501

    OpenAPI spec version: 9.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="TGS API",
    author_email="",
    url="",
    keywords=["Swagger", "TGS API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A production scale tool for BYOND server management  # noqa: E501
    """
)
