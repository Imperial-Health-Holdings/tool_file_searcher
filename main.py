import os
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
list_files_to_check = [path_file1, path_file2]

if file1_exist:
    print(f'{file1} exists.')
else:
    print(f'{file1} does not exist')

if file2_exist:
    print(f'{file2} exists.')
else:
    print(f'{file2} does not exist') 


# mailer with conditions