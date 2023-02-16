# setup file to compile SIR Module

from setuptools import setup
import sys, os
import setuptools

this_dir = os.path.dirname(os.path.realpath(__file__))

__version__ = '0.0.0'


setup(
    name='sir',
    version=__version__,
    author='Jinfei Zhu, Toka Tarek, Tori Sauve, Yuetong Bai',
    author_email='jinfei@uchicago.edu',
    description='a basic example package',
    url="https://github.com/37830Winter2022/final-project-team1",
    python_requires='>=3.6',
    packages=['sir'],
    zip_safe=True,
    install_requires=['numpy', 'scipy','matplotlib', 'pandas']

)
