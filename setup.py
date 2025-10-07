from setuptools import setup, find_packages

setup(
    name='n4s-sdk',  # Nome del pacchetto su PyPI
    version='0.1.0',
    description='A collection of Python SDKs for N4S.io APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ratz',
    url='https://github.com/chiefratz/n4s_sdk_py',  # URL del repository
    packages=find_packages(),  # Include dynamicsdk e sensordatasdk
    install_requires=[
        'requests>=2.28.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)