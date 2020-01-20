

import setuptools
with open("README.md", "r") as fh:
    README = fh.read()

setuptools.setup(
    name="topsis_101883070", 
    version="1.0.1",
    author="Vanshita",
    author_email="vanshitagupta1607@gmail.com",
    description="A Python package to implement topsis function",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vanshita1607/Topsis",
    packages=setuptools.find_packages(),
    licence="MIT" 
)