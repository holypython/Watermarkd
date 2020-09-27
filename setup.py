#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Simple Photo Watermarker with intuitive GUI and common options
# https://github.com/holypython

"""Simple Photo Watermarker"""

from setuptools import setup, find_packages
# from codecs import open
import io
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Watermarkd',
    version="0.8",
    description='Simple Photo Watermarker',
    long_description=long_description,
    url='https://github.com/holypython',
    author='Holypython.com',
    author_email='admin@holypython.com',
    license='Apache',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',


        'Operating System :: OS Independent',
        'Intended Audience :: Photographers',
        'Intended Audience :: Developers',
        'Intended Audience :: Entrepreneurs',
        'Topic :: Office/Business :: Digital Image Processing',
        'Topic :: Office/Business :: Digital Image Processing :: Photography',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    platforms=['any'],
    keywords='watermark, watermarking, photography, image processing, batch image processing, holypython, holypython.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=['pandas>=0.24', 'numpy>=1.15',
                      'random>=x.xx', 'pysimplegui>=x.x.x',
                      'PIL>=x.x.x'],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)