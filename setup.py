
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="stl",
    version="dev",
    author="Martin Atkins",
    author_email="mart@degeneration.co.uk",

    packages=['stl'],
    install_requires=[
    ],
    setup_requires=[
        'nose>=1.0',
        'sphinx>=0.5',
    ],
    tests_require=[
        'nose>=1.0',
        'coverage',
        'mock',
        'pep8',
    ],
    test_suite='nose.collector',
)
