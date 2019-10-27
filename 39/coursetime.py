from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
#urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES,'r') as file:
        data = file.readlines()

    content= list()
    for e in data:
        line = e.strip()
        if line != "":
            content.append(line)
    
    result = list()
    for c in content:
        m = re.match(r"^Start \D* \((\d?\d:\d\d)\)", c)
        if m:
            result.append(m[1])

    return result

def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    td = timedelta()
    for ts in timestamps:
        
        d = datetime.strptime(ts,"%M:%S")
        td += d - datetime.strptime('00:00:00','%H:%M:%S')
    return (datetime.strptime('00:00:00','%H:%M:%S') + td).strftime('%H:%M:%S')

if __name__ == '__main__':
    data = get_all_timestamps()
    calc_total_course_duration(data)
