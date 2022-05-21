from setuptools import setup, find_packages

setup(
    name='aoc2018',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)