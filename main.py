import os
from datetime import datetime
from mailer import mailer
import configparser

def file_searcher():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    config = configparser.ConfigParser()
    config.read('config.ini')

    config_mailer = configparser.ConfigParser()
    config_mailer.read('./mailer/config_mailer.ini')

    # ==== initialization ====
    path_directory = config['PATH']['path_directory']

    # add year, month post_fix to file name
    year_month = str(datetime.now().year) + str(datetime.now().month)
    file1 = config['FILENAME']['file1_prefix'] + f'_{year_month}.xlsx'
    file2 = config['FILENAME']['file2_prefix'] + f'_{year_month}.xlsx'

    # add directory path to filename to create full path
    path_file1 = os.path.join(path_directory, file1)
    path_file2 = os.path.join(path_directory, file2)


    # ==== email parameters ====
    char_month = datetime.now().strftime('%b')

    # SSRS ran successfully
    recipient = config_mailer['MAILER_SUCCESS']['recipient']
    subject = config_mailer['MAILER_SUCCESS']['subject'] + ' ' + char_month
    text = config_mailer['MAILER_SUCCESS']['text']

    # SSRS failed
    recipient_failed = config_mailer['MAILER_FAILED']['recipient']
    subject_failed = config_mailer['MAILER_FAILED']['subject'] + ' ' + char_month


    # ==== look for files in directory ====
    list_files = [path_file1, path_file2]
    list_exist = []
    list_none_exist = []

    # iterate through the list
    for file in list_files:
        if not os.path.exists(file):
            list_none_exist.append(file)
        else:
            list_exist.append(file)

    # mailer with conditions
    if len(list_none_exist) > 0:
        text_failed_header = 'SSRS export failed with following files missing: \n'
        text_failed = text_failed_header + '\n'.join(list_none_exist)

        text_success_header = 'Following reports have been successfully exported: \n'
        text_success = text_success_header + '\n'.join(list_exist)

        text = text_failed + '\n\n' + text_success

        mailer.send_report_notification(recipient_failed, subject_failed, text)
    else:
        mailer.send_report_notification(recipient, subject, text)

if __name__ == '__main__':
    file_searcher()