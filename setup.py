from setuptools import setup, find_packages

setup(
    name="string-calculator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
    ],
    python_requires=">=3.9",
    author="Abhishek Rathore",
    description="String Calculator TDD Kata for Incubyte Assessment",
)
