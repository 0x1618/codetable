from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='codetable',
    version='1.0.8',
    description=
    "Codetable is a lightweight package for seamlessly setting up codes, such as those used in API responses.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Maksymilian Sawicz',
    url='https://github.com/0x1618/codetable',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
