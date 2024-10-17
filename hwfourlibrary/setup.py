from setuptools import setup, find_packages

setup(
    name='hwfour',
    version='0.1',
    packages=find_packages(),
    description='A Python library that facilitates the execution of a homework assignment in Computing for DS',
    author='Anastasiia Chernavskaia, Soledad Monge, Matias Borrell',
    author_email='anastasiia.chernavskaia@bse.eu', 'soledad.monge@bse.eu', 'matias.borrell@bse.eu',
    url='https://github.com/soledadmonge/hw4/hwfourlibrary',
    install_requires=[functools, pandas, datetime, numpy]
)
