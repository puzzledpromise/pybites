import csv

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')
    return decoded_content


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    pass

if __name__ == '__main__':
    get_csv()