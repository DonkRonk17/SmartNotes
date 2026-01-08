#!/usr/bin/env python3
"""
SmartNotes Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="smartnotes",
    version="1.0.0",
    author="Team Brain",
    author_email="logan@metaphysicsandcomputing.com",
    description="AI-Powered Note Taking & Organization - Quick, searchable notes from the command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DonkRonk17/SmartNotes",
    py_modules=["smartnotes"],
    python_requires=">=3.7",
    install_requires=[],  # No external dependencies!
    entry_points={
        "console_scripts": [
            "smartnotes=smartnotes:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Office/Business",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="notes note-taking cli organization tags search productivity",
)
