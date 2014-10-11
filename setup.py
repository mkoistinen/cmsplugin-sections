#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# To register app to PyPI:
# python setup.py register -r pypi
#
# NOTE: To update PyPI, tag the current release:
#
# First increment cache_tools/__init__.py
# Then:
# > git tag x.y.z -m "Version bump for PyPI"
# > git push --tags origin master
# Then:
# > python setup.py sdist upload
#

from setuptools import setup, find_packages
from cmsplugin_sections import __version__


INSTALL_REQUIRES = [
    'Django>=1.7.0',
    'django-cms>=3.0.6',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='cmsplugin-sections',
    version=__version__,
    description='Plugins to aide creating “single page scroller” websites.',
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    url='https://github.com/mkoistinen/cmsplugin-sections',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False,
    download_url='https://github.com/mkoistinen/cmsplugin-sections/tarball/0.0.1',
)