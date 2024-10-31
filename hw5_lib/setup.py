from setuptools import setup, find_packages

setup(
    name='hw5_lib', 
    version='0.1.0',
    description='Library for hw5.py',
    author='Matias Borrell, Nastia Cher, Soledad Monge',
    author_email='matias.borrell@bse.eu, nastia.cher@bse.eu, soledad.mong@bse.eu',
    url='https://github.com/ananstr/hw_5', 
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
    ], 
)