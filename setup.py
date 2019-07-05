from setuptools import setup, find_packages


with open("README.md") as fp:
    long_description = fp.read()

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

with open("VERSION") as fp:
    version = fp.read().strip()

setup(
    name='book-models',
    license='MIT',
    version=version,
    description='Library which contains models related to books.',
    long_description=long_description,
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    author='Moloce Adrian',
    author_email='moloce.ady@gmail.com',
    url='https://github.com/MoloceAdrian/book-models',
)
