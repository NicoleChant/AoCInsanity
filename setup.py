from setuptools import setup , find_packages
from pathlib import Path

with open("requirements.txt" , encoding = "utf-8" , mode = "r+") as f:
    requirements = [line.strip() for line in f.readlines()]


setup(
    author = "Channi",
    version = "1.0.0",
    name = "pyaoc",
    description = "A python package for AoC solutions! (Artistic!)",
    install_requires = requirements,
    packages = find_packages()
)
