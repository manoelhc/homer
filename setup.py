#!/usr/bin/env python3

from distutils.core import setup

version = "0.0.1"

setup(
    name = 'homer',
    packages = ['homer'],
    license = 'MIT',
    version = version,
    description = 'Homer is a config handler tool.',
    author = 'Manoel Carvalho',
    author_email = 'manoelhc@gmail.com',
    url = 'https://github.com/manoelhc/homer', # use the URL to the github repo
    download_url = 'https://github.com/manoelhc/homer', # I'll explain this in a second
    keywords = ['testing', 'configuration'], # arbitrary keywords
    install_requires=[
        'Crypto'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
