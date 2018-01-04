import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requirements = (
    'flask==0.11.1',
    'uwsgi==2.0.15',
    'Flask-Bootstrap==3.3.7.1'
)

setup(
    name='app',
    version='1.0.0',
    description="Application",
    author='dev',
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements,
    include_package_data=True,
)
