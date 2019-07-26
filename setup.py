# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.0.1'

with open('requirements.txt') as f:
	requirements = f.read().strip().split('\n')

setup(
	name='vidya',
	version=version,
	description='Open Source AIML Bot',
	author='Frappe',
	author_email='hello@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=requirements
)
