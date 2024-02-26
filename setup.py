from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(requirement_file:str)->List[str] :
    """
        this function will return the list of requirements
    """
    with open(requirement_file) as file:
        requirements = [package for package in file.read().split("\n")]

        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Abhinav",
    author_email="abhinava8requirements@gmail.com",
    packages=find_packages(), #Checks which folders have __init__.py and then builds the package
    install_requires=get_requirements("requirements.txt")
)