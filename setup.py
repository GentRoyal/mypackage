from setuptools import setup, find_packages

# Load the README file content for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(exclude=["tests*", "docs", "examples"]),
    license="MIT",
    description="A Python package with mathematical utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy>=1.18.0"  # Define minimum version for compatibility
    ],
    extras_require={
        "dev": ["pytest", "flake8"],  # Additional packages for development
    },
    url="https://github.com/<username>/<package-name>",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Development Status :: 3 - Alpha",  # Change this as your project evolves
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",
    project_urls={
        "Bug Tracker": "https://github.com/<username>/<package-name>/issues",
        "Documentation": "https://github.com/<username>/<package-name>/wiki",
        "Source Code": "https://github.com/<username>/<package-name>",
    },
    keywords="math utilities EDSA example package",
)
