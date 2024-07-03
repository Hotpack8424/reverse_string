from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="reverse_string",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple package to reverse strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/reverse_string",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # 'somepackage>=1.0.0',
    ],
)
