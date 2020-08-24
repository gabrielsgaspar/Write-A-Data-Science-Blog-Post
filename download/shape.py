#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this script is to programatically download shapefiles
from the World Bank database and save them
"""

# Import libraries
import requests
import os
from zipfile import ZipFile

# Define function to download shapefiles
def download_shape(path):
    '''Downloads zip files that contains shapefile data from
    IPSUM's website
    '''
    url = 'https://international.ipums.org/international/resources/gis/IPUMSI_world_release2017.zip'
    r = requests.get(url)
    open(str(path + '/shapes.zip'), 'wb').write(r.content)

# Define function to unzip file
def unzip_shp(zip_name, shp_name):
    '''Unizps files from download_shape function, extracts only the shp file
       and saves them
    '''
    # Print progress
    print('Unzipping', zip_name, '...', end = '\r')
    # Open zipfile and get only shapefile
    with ZipFile(zip_name) as zf:
        with zf.open(shp_name, 'r') as infile:
            # TODO

# Define function to delete zip files
def remove(ext):
    '''Deletes files with the passed argument in current
       working directory
    '''
    # Get directory
    dir = os.getcwd()
    # Get files in directory in list
    files = os.listdir(dir)
    # Loop to find files with extension and delete
    for file in files:
        if file.endswith(ext):
            os.remove(os.path.join(dir, file))

if __main__ == '__main__':
    # Create data directory if it doesn't exist and change directory
    if not os.path.exists('../data/shapefile'):
        os.makedirs('../data/shapefile')
        os.chdir('../data/shapefile')
    else:
        os.chdir('../data/shapefile')
    # Set variables
    zip_name = 'shapes.zip'
    shp_name = 'world_countries_2017.shp'
    # Get working directory
    path = str(os.getcwd())
    # Call function to download files
    download_shape(path)
    # Call functio to extract data
    unzip_shp(zip_name, shp_name)
    # Delete zip files
    remove('.zip')
