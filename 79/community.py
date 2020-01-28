import csv
from collections import Counter

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)

    return download.content.decode('utf-8')



def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    data = list()
    for l in content.splitlines():
        _, _, area = l.split(',')
        data.append(area)
    count_data = Counter(data)
    del count_data["tz"]
    count = sorted(list(count_data.items()))
    for area, n in count:
        print(area.ljust(20) + "|" + n * "+")



if __name__ == "__main__":
    content = get_csv()
    create_user_bar_chart(content)
