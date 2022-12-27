from datetime import date
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile
from pathlib import Path
import os

S3 = "https://bites-data.s3.us-east-2.amazonaws.com"

TMP = Path(os.getenv("TMP", "/tmp"))

def download_test_files():
    data_zipfile = 'bite328_test_data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)

if __name__ == "__main__":
    download_test_files()
