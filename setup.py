from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="stock-analysis-tool",
    version="1.0.0",
    author="Stock Analysis Developer Team",
    author_email="founder@nandurstudio.com",
    description="Stock Analysis and Trading Recommendation Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nandurstudio/stock-analysis",packages=find_packages(include=['src', 'src.*']),
    package_data={
        'src': ['**/*.json', '**/*.csv'],
        '': ['developer_info.txt'],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "stock-analyzer=src.main:main",
        ],
    },
)
