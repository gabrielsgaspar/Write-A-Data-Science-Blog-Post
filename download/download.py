#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this script is to programatically download data
from the Stack Overflow Annual Developer Survey and save it in
the data folder as zip files
"""

# Import libraries
import itertools
from google_drive_downloader import GoogleDriveDownloader as gdd

# Define function to download data
def get_data(path, ids, names):
    ''' Downloads csv files for all available Stack Overflow
        Annual Developer Survey years and saves in specified path
    '''
    # Donwload and save data
    for (id, name) in zip(ids, names):
        gdd.download_file_from_google_drive(file_id = id, dest_path = path + name, unzip = False)

if __name__ == '__main__':
    # Set path where data will be saved
    path = '/Users/gabrielsgaspar/Projects/personal_projects/Write-A-Data-Science-Blog-Post/data/'
    # Set file ids
    ids = ['1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB', '1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV',
            '1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U', '0B6ZlG_Eygdj-c1kzcmUxN05VUXM',
            '0B0DL28AqnGsrV0VldnVIT1hyb0E', '0B0DL28AqnGsra1psanV1MEdxZk0',
            '0B0DL28AqnGsrempjMktvWFNaQzA', '0B0DL28AqnGsrenpPNTc5UE1PYW8',
            '0B0DL28AqnGsrX3JaZWVwWEpHNWM', '0Bx0LyhBTBZQgUGVYaGx3SzdUQ1U']
    # Set file names
    names = ['developer_survey_2020.zip', 'developer_survey_2019.zip', 'developer_survey_2018.zip',
            'developer_survey_2017.zip', 'developer_survey_2016.zip', 'developer_survey_2015.zip',
            'developer_survey_2014.zip', 'developer_survey_2013.zip', 'developer_survey_2012.zip',
            'developer_survey_2011.zip']
    get_data(path, ids, names)
