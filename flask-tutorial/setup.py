#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 05:46:12 2019

@author: kazzastic
"""

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)