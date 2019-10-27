from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    result = []
    with open(COURSE_TIMES,'r') as f:
        for l in f.readlines():
            m = re.match("Start  ([A-Za-z ?]*) \((\d:\d\d)\)", l.strip())
            if m:
                result.append(m[2])
    return result
                


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    zerodate = datetime(1900, 1, 1)
    ds = [datetime.strptime(s,'%H:%M') for s in timestamps]
    dss = [d - zerodate for d in ds]
    result = timedelta(hours=0)
    for d in dss:
        result += d
    format_date = datetime(1900,1,1) + result
    return(f"{format_date:%-H:%M:%S}")
