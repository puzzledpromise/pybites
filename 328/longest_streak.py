import json
from dateutil.tz import gettz
from dateutil.parser import parse
from datetime import date, timedelta, tzinfo
from pathlib import Path
from typing import Tuple, Optional, List
from collections import namedtuple
import os

Streak = namedtuple('Streak', ['start_date', 'end_date', 'count'])

DATA_FILE_NAME = "test4.json"
TMP = Path(os.getenv("TMP", "/tmp"))
DATA_PATH = TMP / DATA_FILE_NAME
MY_TZ = gettz("America/New York")
UTC = gettz("UTC")


def longest_streak(
    data_file: Path = DATA_PATH, my_tz: Optional[tzinfo] = MY_TZ
) -> Optional[Tuple[date, date]]:
    """Retrieve datetime strings of passed commits and calculate the longest
    streak from the user's data

    Note: The datetime strings will need to be used to create aware datetime objects

    All datetimes are in UTC, and the timezone of the user is part of the context
    for calculating a streak. Ex: 2019-10-14 01:58:48.129585+00:00 is 2019-10-13 in
    New York City. You will need to convert datetimes from UTC into the supplied timezone.

    The tests show an example of how a streak can change based on the timezone used.

    If the dataset has two or more streaks of the same length as longest, provide
    only the most recent streak.

    Return a tuple containing start and end date for the longest streak
    or None
    """
    with open(data_file) as f:
        data = json.load(f)
    
    commit_dates = [parse(c['date']) for c in data['commits'] if c['passed'] == True]
    commit_dates = [c.astimezone(my_tz).date() for c in commit_dates]
    commit_dates = sorted(list(set(commit_dates)))

    if not commit_dates:
        return None
    
    streaks = []
    current_streak = None
    for d in commit_dates:
        if not current_streak:
            current_streak = Streak(d, d, 1)
        else:
            if d == current_streak.end_date + timedelta(days=1):
                current_streak = current_streak._replace(end_date=d)
                current_streak = current_streak._replace(count=current_streak.count+1)
            else:
                streaks.append(current_streak)
                current_streak = Streak(d, d, 1)
    streaks.append(current_streak)
    streaks = sorted(streaks, key = lambda x: (x.count, x.end_date))

    return streaks[-1].start_date, streaks[-1].end_date




if __name__ == "__main__":
    streak = longest_streak()
    print(f"My longest streak went from {streak[0]} through {streak[1]}")
    print(f"The streak lasted {(streak[1]-streak[0]).days + 1} days")
