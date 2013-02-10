#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from html_cleaner import VERSION, PROJECT


MODULE_NAME = 'html-cleaner'
PACKAGE_NAME = 'html_cleaner'
PACKAGE_DATA = list()

def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''


META_DATA = dict(
    name = PROJECT,
    version = VERSION,
    description = read('DESCRIPTION'),
    long_description = read('README.rst'),
    license='MIT',

    author = "Illia Polosukhin",
    author_email = "ilblackdragon@gmail.com",

    url = "http://github.com/ProstoKSI/html-cleaner.git",

    packages = find_packages(),
    package_data = { '': PACKAGE_DATA, },

    install_requires = [ 
                       ],
)

if __name__ == "__main__":
    setup( **META_DATA )

