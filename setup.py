#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

try:
    README = open('README.md', encoding='utf-8').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt', encoding='utf-8').read()
except:
    REQUIREMENTS = None

setup(
    name='django-la-contact-form',
    version="v0.1.0",
    description=(
        'Django app for a simple contact form'
    ),
    long_description=README,
    install_requires=REQUIREMENTS,
    author='Fábio Piovam Elias',
    author_email='fabio@laborautonomo.org',
    url='https://github.com/laborautonomo/django-la-contact-form/',
    packages=find_packages(),
    include_package_data=True,
)