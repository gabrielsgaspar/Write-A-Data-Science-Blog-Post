#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this script is to programatically download data
from the Stack Overflow Annual Developer Survey as zip files, open
these files and save the relevant csv files
"""

# Import libraries
import csv
import itertools
import os
from google_drive_downloader import GoogleDriveDownloader as gdd
from io import TextIOWrapper
from zipfile import ZipFile

# Define function to download data
def get_data(path, ids, zip_names):
    ''' Downloads csv files for all available Stack Overflow
        Annual Developer Survey years and saves in specified path
    '''
    # Donwload and save data
    for (id, name) in zip(ids, zip_names):
        gdd.download_file_from_google_drive(file_id = id, dest_path = path + name, unzip = False)

# Define function to unzip and save csv
def unzip_csv(zip_names, csv_names, new_names):
    '''Unzips files extracted in get_data function,
       extracts only relevant csvs and saves them
    '''
    # Set data directory
    os.chdir('../data')
    # Open zip files
    for (zip_name, csv_name, new_name) in zip(zip_names, csv_names, new_names):
        with ZipFile(zip_name) as zf:
            with zf.open(csv_name, 'r') as infile:
                file = csv.reader(TextIOWrapper(infile, 'utf-8'))
                # Open as writer
                with open(new_name, 'w') as new_file:
                    writer = csv.writer(new_file)
                    # Loop over to save
                    for line in file:
                        writer.writerow(line)

if __name__ == '__main__':
    # Set path where data will be saved
    path = '/Users/gabrielsgaspar/Projects/personal_projects/Write-A-Data-Science-Blog-Post/data/'
    # Set file ids
    ids = ['1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB', '1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV',
            '1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U', '0B6ZlG_Eygdj-c1kzcmUxN05VUXM',
            '0B0DL28AqnGsrV0VldnVIT1hyb0E', '0B0DL28AqnGsra1psanV1MEdxZk0',
            '0B0DL28AqnGsrempjMktvWFNaQzA', '0B0DL28AqnGsrenpPNTc5UE1PYW8',
            '0B0DL28AqnGsrX3JaZWVwWEpHNWM', '0Bx0LyhBTBZQgUGVYaGx3SzdUQ1U']
    # Set file zip names
    zip_names = ['developer_survey_2020.zip', 'developer_survey_2019.zip', 'developer_survey_2018.zip',
            'developer_survey_2017.zip', 'developer_survey_2016.zip', 'developer_survey_2015.zip',
            'developer_survey_2014.zip', 'developer_survey_2013.zip', 'developer_survey_2012.zip',
            'developer_survey_2011.zip']
    # Set name of csv files
    csv_names = ['survey_results_public.csv', 'survey_results_public.csv', 'survey_results_public.csv',
                'survey_results_public.csv', '2016 Stack Overflow Survey Responses.csv', '2015 Stack Overflow Developer Survey Responses.csv',
                '2014 Stack Overflow Survey Responses.csv', '2013 Stack Overflow Survey Responses.csv',
                '2012 Stack Overflow Survey Results.csv', '2011 Stack Overflow Survey Results.csv']
    # Set new csv names
    new_names = ['survey_2020.csv', 'survey_2019.csv', 'survey_2018.csv',
            'survey_2017.csv', 'survey_2016.csv', 'survey_2015.csv',
            'survey_2014.csv', 'survey_2013.csv', 'survey_2012.csv',
            'survey_2011.csv']
    # Call function to download data
    get_data(path, ids, zip_names)
    # Call function to extract data
    unzip_csv(zip_names, csv_names, new_names)
