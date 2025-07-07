from setuptools import find_packages, setup

setup(
    name="yyyoink-llm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "black",
        "isort",
    ],
    entry_points={
        "console_scripts": [
            "llm = src.main:main",
        ],
    },
)
