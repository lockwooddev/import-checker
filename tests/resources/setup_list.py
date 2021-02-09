from setuptools import setup


__version__ = '4.0.0'


setup(
    name='setup-test',
    version=__version__,
    install_requires=[
        'requests==2.23.0',
        'markdown',
    ],
)
