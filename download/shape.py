#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this script is to programatically download shapefiles
from the World Bank database and save them
"""

# Import libraries
import requests

# Define function to download shapefiles
def download_shape(path):
    # TODO


if __main__ == '__main__':
    # Create data directory if it doesn't exist and change directory
    if not os.path.exists('../data/shapefiles'):
        os.makedirs('../data/shapefiles')
        os.chdir('../data/shapefiles')
    else:
        os.chdir('../data/shapefiles')
    download_shape()
