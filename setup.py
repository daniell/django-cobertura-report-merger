import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-cobertura-report-merger',
    version='0.0.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=['django>=1.8'],
    tests_require=['pytest', 'mock'],
    include_package_data=True,
    license='GPLv3',
    description='A django app to merge cobertura coverage reports',
    long_description=README,
    url='https://www.github.com/daniell/',
    author='Daniel Levy',
    author_email='daniell@aptivate.org',
    classifiers=[
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
