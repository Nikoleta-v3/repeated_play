from setuptools import find_packages, setup

# Read in the version number
exec(open("src/stationary/version.py", "r").read())

setup(
    name="stationary",
    version=__version__,
    author="Nikoleta Glynatsi",
    author_email=("glynatsi@evolbio.mpg.de"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    description="A package for calculating stationary distributions of Markov processes.",
)
