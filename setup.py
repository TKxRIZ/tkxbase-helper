from setuptools import setup, find_packages

setup(
    name="tkxbase-helper",
    version="1.0.0",
    description="CLI Helper Toolkit für Admin-Login, farbige Ausgaben und File-Handling.",
    author="TK",
    author_email="deine@email.com",
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)