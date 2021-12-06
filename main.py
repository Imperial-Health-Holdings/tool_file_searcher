import os
from datetime import datetime

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# initialization
path_directory = config['PATH']['path_directory']

year_month = str(datetime.now().year) + str(datetime.now().month)
file1 = config['FILENAME']['file1_prefix'] + f'_{year_month}.xlsx'
file2 = config['FILENAME']['file2_prefix'] + f'_{year_month}.xlsx'

# look for files in directory
if os.path.exists(os.path.join(path_directory, file1)):
    print(f'{file1} exists.')
else:
    print(f'{file1} does not exist')

if os.path.exists(os.path.join(path_directory, file2)):
    print(f'{file2} exists.')
else:
    print(f'{file2} does not exist') 


# mailer with conditions