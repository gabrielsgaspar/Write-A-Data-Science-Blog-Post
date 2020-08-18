#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this script is to programatically download shapefiles
from the World Bank database and save them
"""

# Import libraries
import requests
import os

# Define function to download shapefiles
def download_shape(path):
    '''Downloads, unzips and saves shapefile data from 
    IPSUM's website
    '''
    #https://international.ipums.org/international/resources/gis/IPUMSI_world_release2017.zip

if __main__ == '__main__':
    # Create data directory if it doesn't exist and change directory
    if not os.path.exists('../data/shapefile'):
        os.makedirs('../data/shapefile')
        os.chdir('../data/shapefile')
    else:
        os.chdir('../data/shapefile')
    # Get working directory
    path = str(os.getcwd())
    # Call function to download files
    download_shape(path)
