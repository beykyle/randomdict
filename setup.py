#!/usr/bin/env python

from setuptools import setup
import beykylerandomdict

V = beykylerandomdict.__version__

setup(name='beykylerandomdict',
      version=V,
      author='Kyle Beyer',
      author_email='beykyle@umich.edu',
      url='https://github.com/beykyle/randomdict',
      long_description="""
      python `dict` compatible object with fast, O(1), random access to keys and values. Originally written by Rob Tandy.
      """,
      py_modules=['beykylerandomdict'],
      setup_requires=['nose>=1.0'],
)
