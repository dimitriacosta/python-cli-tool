"""
Install the jarvis CLI tool
"""
from setuptools import setup, find_packages


def read_requirements():
    """Install the requirements from the txt file"""
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    name='jarvis',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        jarvis=src.cli:cli
    '''
)
