import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# NOTE: Avoid IDE errors, actual version is read from version.py
__version__ = None
with open("utils_plus/version.py") as f:
    exec(f.read())

setuptools.setup(
    name="utils_plus",
    version=__version__,
    author="KunLin Lee",
    author_email="LeeKLTW@gmail.com",
    description="Useful plugins for utils.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeeKLTW/utils_plus",
    packages=setuptools.find_packages(),
    classifier=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
