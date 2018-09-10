#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='srun',
        version='0.0.1',
        description='Server run',
        author='yk',
        packages=find_packages(),
        scripts=['bin/srun'],
        install_requires=['sh', 'fabric'],
        )
