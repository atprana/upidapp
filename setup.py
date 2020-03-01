# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in upidapp/__init__.py
from upidapp import __version__ as version

setup(
	name='upidapp',
	version=version,
	description='Unipres Indonesia ERPNext Customization',
	author='atprana',
	author_email='atprana.develop@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
