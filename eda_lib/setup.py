from setuptools import setup, find_packages

setup(
    name='eda_lib',
    version='1.0',
    description='Small set of tools for EDA',
    author='Matias Borrell, Nastia Cher, Soledad Monge',
    author_email='anastasiia.chernavskaia@bse.eu, soledad.monge@bse.eu, matias.borrell@bse.eu',
    license='MIT',
    packages=find_packages(), 
    install_requires=['pandas', 'numpy', 'scikit-learn'], 
)