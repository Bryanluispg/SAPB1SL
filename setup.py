################################################
#                   BLPG                       #   
################################################

from setuptools import setup, find_packages

setup(
    name="SAPB1SL",
    version="1.3.0",
    author="Bryan Pineda Gonzalez",
    author_email="dev@bryanlpinedag.com",
    description="Cliente Python para el Service Layer de SAP Business One usando requests.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bryanluispg/SAPB1SL",  
    packages=find_packages(),
    install_requires=[
        "requests",
        "urllib3"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
