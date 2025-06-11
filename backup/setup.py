from setuptools import setup, find_packages

setup(
    name='stock-analysis',
    version='0.1.0',
    author='Nandur Studio',
    author_email='founder@nandurstudio.com',
    description='A project for stock analysis, prediction, and visualization.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.24.0',
        'pandas>=2.0.0',
        'yfinance>=0.2.18',
        'scikit-learn>=1.2.0',
        'matplotlib>=3.7.0',
        'seaborn>=0.12.0',
        'ta>=0.10.0',
        'keyboard>=0.13.5'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)