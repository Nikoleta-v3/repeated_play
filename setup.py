from setuptools import find_packages, setup

# Read in the version number
exec(open("src/repeated_play/version.py", "r").read())

setup(
    name="repeated_play",
    version=__version__,
    author="Nikoleta Glynatsi",
    author_email=("glynatsi@evolbio.mpg.de"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    description="A package.",
)
