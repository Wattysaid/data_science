# setup.py
from setuptools import setup, find_packages

setup(
    name='data_science',
    version='0.1',
    packages=find_packages(),
    description='A collection of data science code snippets.',
    author='Kieran F. Noonan',
    author_email='kieran.francis.noonan@gmail.com',
    url='https://github.com/Wattysaid/data_science',
    install_requires=[
        # List your package dependencies here
      pandas, numpy
    ],
)
