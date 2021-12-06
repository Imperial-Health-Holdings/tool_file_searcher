import os
import pandas as pd
from datetime import datetime
from mailer import mailer

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# ==== initialization ====
path_directory = config['PATH']['path_directory']

# add year, month post_fix to file name
year_month = str(datetime.now().year) + str(datetime.now().month)
file1 = config['FILENAME']['file1_prefix'] + f'_{year_month}.xlsx'
file2 = config['FILENAME']['file2_prefix'] + f'_{year_month}.xlsx'

# add directory path to filename to create full path
path_file1 = os.path.join(path_directory, file1)
path_file2 = os.path.join(path_directory, file2)

# ==== look for files in directory ====
list_files = [path_file1, path_file2]
list_none_exist = []

# iterate through the list
for file in list_files:
    if not os.path.exists(file):
        list_none_exist.append(file)

# mailer with conditions
