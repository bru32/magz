"""
magz package

To install package run:
  python setup.py install

Bruce Wernick
08 October 2017 7:11:27
"""

from setuptools import setup, find_packages

with open('README.rst') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='magz',
  version='0.1.0',
  description='TechniSolve tools package',
  long_description=readme,
  author='Bruce Wernick',
  author_email='info@coolit.co.za',
  url='c:/code/python/magz',
  license=license,
  platforms=['Windows'],
  packages=find_packages(exclude=('tests','docs','dev'))
)

