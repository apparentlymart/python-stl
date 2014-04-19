
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="stl",
    version="0.0.1",
    author="Martin Atkins",
    author_email="mart@degeneration.co.uk",
    description="Read and write STL 3D geometry files in both the ASCII and the binary flavor",

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

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)
