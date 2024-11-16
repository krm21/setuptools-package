from setuptools import setup, find_packages

setup(
    name="my_package", 
    version="0.1.0",  
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/krm21/setuptools-package",
    packages=find_packages(), 
    install_requires=[
        "pandas==2.2.2", 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
