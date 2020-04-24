
april_1981 = """     april 1981
su mo tu we th fr sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

jan_1986 = """    january 1986
su mo tu we th fr sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

jan_1956 = """    january 1956
su mo tu we th fr sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""

weekdays = ['Su','Mo','Tu','We','Th','Fr','Sa','Su']

def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines = calendar_output.split('\n')[2:]
    result = dict()
    for line in lines:
        for index in range(0,len(line),3):
            weekday = weekdays[index//3]
            num = line[index:index+2]
            try:
                i = int(num)
                result[i] = weekday
            except ValueError:
                continue
    return result


if __name__ == "__main__":
    get_weekdays(april_1981)
