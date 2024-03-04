# setup.py

from setuptools import setup, find_packages

setup(
    name='mympl',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',  # Ensure matplotlib is installed as a dependency
    ],
)
