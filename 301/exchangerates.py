import os
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
from dateutil.parser import parse

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    result_dates = list()
    d = start_date
    while(d <= end_date):
        result_dates.append(d)
        d = d + timedelta(days=1)
    return result_dates

def get_daily_rates(location=RATES_FILE):
    with open(RATES_FILE,'r') as json_file:
            data = json.load(json_file)
    result_dict = dict()

    for d in data['rates'].keys():
        result_dict[d] = dict()
        result_dict[d]["USD"] = data['rates'][d]['USD']
        result_dict[d]["GBP"] = data['rates'][d]['GBP']

    return result_dict



def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    dates_rate = sorted([parse(d).date() for d in daily_rates.keys()])
    if start < dates_rate[0] or end > dates_rate[-1]:
        raise ValueError()
    
    dates = get_all_days(start, end)
    result_dict = dict()
    for ds in dates:
        d = f"{ds:%Y-%m-%d}"  
        if d in daily_rates:
            result_dict[d] = d
        else:
            x = ds
            while(True):
                x = x + timedelta(days=-1)
                if f"{x:%Y-%m-%d}" in daily_rates:
                    result_dict[d] = x
                    break

    return result_dict


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    start_date = parse(start_date).date()
    end_date = parse(end_date).date()

    daily_rates = get_daily_rates()
    dates = get_all_days(start_date, end_date)
    match_dict = match_daily_rates(start_date, end_date, daily_rates)

    result_dict = dict()
    for d in dates:
        focusdate = match_dict[d]
        result_dict[d] = daily_rates[f"{focusdate:%Y-%m-%d}"]
        result_dict[d]["Base Date"] = focusdate

    return result_dict

if __name__ == '__main__':
    result = exchange_rates()
    result = match_daily_rates(date(2020,1,1), date(2020,9,1))
    print(result)
