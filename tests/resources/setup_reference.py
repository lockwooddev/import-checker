from setuptools import setup


__version__ = '4.0.0'

install_requirements = [
    'requests==2.23.0',
    'markdown',
]

setup(
    name='setup-test',
    version=__version__,
    install_requires=install_requirements,
)
