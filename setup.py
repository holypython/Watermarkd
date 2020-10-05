#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Simple Photo Watermarker with intuitive GUI and common options
# https://github.com/holypython

"""Simple Photo Watermarker"""

import setuptools
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='Watermarkd',
   version='0.7.2.1',
   description='A friendly watermarking tool with optional GUI component.',
   license="Apache-2.0",
   long_description=long_description,
   author='holypython.com',
   author_email='watermarkd@holypython.com',
   url="https://holypython.com/",
   download_url = 'https://github.com/holypython/Watermarkd/archive/0.7.2.1.tar.gz',
   packages=['Watermarkd'],
   keywords = ['watermarking', 'image processing', 'watermark', 'photography', 'copyrights', 'holypython', 'batch watermark', 'holypython.com'],
   classifiers=[
       "Development Status :: 3 - Alpha",
       "Intended Audience :: Developers",
       "Intended Audience :: Education",
       "Intended Audience :: End Users/Desktop",
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: Apache Software License",
       "Operating System :: OS Independent",
   ],

   install_requires=[
       'pillow',
       'pysimplegui',
   ],

   python_requires='>=3.6'
)
