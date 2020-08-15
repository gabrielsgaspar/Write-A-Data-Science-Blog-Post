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
    # http://gisco-services.ec.europa.eu/distribution/v2/countries/download/ref-countries-2020-01m.shp.zip
    # https://international.ipums.org/international/gis.shtml

if __main__ == '__main__':
    # Create data directory if it doesn't exist and change directory
    if not os.path.exists('../data/shapefile'):
        os.makedirs('../data/shapefile')
        os.chdir('../data/shapefile')
    else:
        os.chdir('../data/shapefile')
    download_shape()
