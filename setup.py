# -*- coding: utf-8 -*-
"""
Realtime-Import
-------------

import the modules in every funciton calling if you need
"""

from setuptools import setup

setup(
    name='Realtime-Import',
    version='0.0.1.dev0',
    url='https://github.com/caimaoy/realtime',
    license='BSD',
    author='caimaoy',
    keywords=['function', 'realtime', 'import'],
    author_email='i@caimaoy.com',
    description='import the modules in every funciton calling',
    long_description=__doc__,
    py_modules=['realtime'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['realtime'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ])
