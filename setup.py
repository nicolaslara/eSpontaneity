#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='espontaneity',
      version='0.1',
      packages=find_packages(),
      package_data={'espontaneity': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'espontaneity': ['bin/*.pyc']},
      scripts=['espontaneity/bin/manage.py'])
