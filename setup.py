from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return list of requirements
    """
    requirements = []
    with open(file_path) as f:
        for line in f:
            if line==hyphen_e_dot:
                continue
            word = line.strip()
            requirements.append(word)
        
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sagar',
    author_email='agrawalsagar5663@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn']
    install_requires= get_requirements('requirements.txt') # use this line instead of above line
)