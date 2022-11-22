from collections import namedtuple
import datetime
import sys

import feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return datetime.date(stime.tm_year, stime.tm_mon, stime.tm_mday)


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    d = feedparser.parse(feed)
    result = []
    for e in d.entries:
        ts = e['published_parsed']
        dt = _convert_struct_time_to_dt(ts) 
        title = e['title']
        link = e['link']
        tags = []
        for t in e['tags']:
            tags.append(t['term'].lower())

        entry = Entry(dt, title, link, tags)
        result.append(entry)
    return result


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    if "&" in search:
        search_tags = search.split("&")
        for s in search_tags:
            if not filter_entries_by_tag(s, entry):
                return False
        return True
    if "|" in search:
        search_tags = search.split("|")
        for s in search_tags:
            if filter_entries_by_tag(s, entry):
                return True
    return search.lower() in entry.tags

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()
    while(True):
        search_term = input("Please enter a search term: ")
        if search_term.lower().strip() == "":
            print("Please provide a search term")
            continue
        if search_term.lower() == "q":
            print("Bye")
            return
        result = []
        for e in entries:
            if filter_entries_by_tag(search_term, e):
                result.append(e)

        result.sort(key=lambda x: x.date)
        for r in result:
            print(r.title)
        n = len(result)
        if n == 1:
            print(f"{n} entry matched")
        else: 
            print(f"{n} entries matched")


if __name__ == '__main__':
    main()
