#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this script is to programatically download data
from the Stack Overflow Annual Developer Survey and save it in
the data folder
"""

# Import libraries
import os
import requests


def get_data(path):
    ''' Downloads csv files for all available Stack Overflow
        Annual Developer Survey years and saves in specified path
    '''
    # Set url for survey years
    url_2020 = 'https://drive.google.com/file/d/1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB/view?usp=sharing'
    url_2019 = 'https://drive.google.com/open?id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV'
    url_2018 = 'https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U'
    url_2017 = 'https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM'
    url_2016 = 'https://drive.google.com/uc?export=download&id=0B0DL28AqnGsrV0VldnVIT1hyb0E'
    url_2015 = 'https://drive.google.com/uc?export=download&id=0B0DL28AqnGsra1psanV1MEdxZk0'
    url_2014 = 'https://drive.google.com/uc?export=download&id=0B0DL28AqnGsrempjMktvWFNaQzA'
    url_2013 = 'https://drive.google.com/uc?export=download&id=0B0DL28AqnGsrenpPNTc5UE1PYW8'
    url_2012 = 'https://drive.google.com/uc?export=download&id=0B0DL28AqnGsrX3JaZWVwWEpHNWM'
    url_2011 = 'https://drive.google.com/uc?export=download&id=0Bx0LyhBTBZQgUGVYaGx3SzdUQ1U'
    # Donwload data
    ## # TODO:
    # Save data
    ## # TODO:

if __name == '__main__':
    path = os.chdir("../data")
    get_data()
