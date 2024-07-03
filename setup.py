from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="GrantingUNOB",  
    version="0.0.1",
    author="Tran Hieu Duc, To Minh Quan",
    author_email="heovip1ad@gmail.com",
    description="A package for extracting and processing Cyber Security program data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hieuducemo/Granting-database",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "beautifulsoup4",
        "selenium",
        "webdriver-manager"
    ],
)
