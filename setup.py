from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.md').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='mmovies.migration',
      version=version,
      description="Import IMDB plain text data to Mongo",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Marco Mariani',
      author_email='birbag@gmail.com',
      url='https://github.com/mmariani/mmovies.migration',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['mmovies'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'pymongo',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      mmovies-import = mmovies.migration.plainimport:main
      """,
      )
