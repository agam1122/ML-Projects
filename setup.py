from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path):
    """
    Reads the requirements from a file and returns them as a list.
    """
    with open(file_path, "r") as f:
        requirements = f.read().splitlines()
        
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(    name="ML_Project",
    version="0.1.0",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    description="ML Project in Python",
    author="Agam Partap Singh",
    
)