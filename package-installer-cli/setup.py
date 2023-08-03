from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="package-installer",
    version="0.1.0",
    author="Your Name",
    author_email="your@email.com",
    description="A Python package installer CLI and GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/package_installer",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "package-installer-cli = package_installer.installer:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
