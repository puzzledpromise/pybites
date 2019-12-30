from collections import namedtuple
from operator import attrgetter
import datetime
from datetime import date, datetime
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
    return date(stime.tm_year, stime.tm_mon, stime.tm_mday)


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       return a list of entry namedtuples (date = date, drop time part)
    """
    d = feedparser.parse(feed)
    results = []
    for entry in d.entries:
        time_struct = entry.published_parsed
        published = _convert_struct_time_to_dt(time_struct)
        tags = [t.term.lower() for t in entry.tags]
        e = Entry(published, entry.title, entry.link, tags)
        results.append(e)

    #results = sorted(results, key=attrgetter('date'))

    return results


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
    search = search.lower()
    
    if "&" in search:
        kw = search.split("&")
        for e in entry.tags:
            for s in kw:
                    if s not in entry.tags:
                        return False
        return True
    elif "|" in search:
        kw = search.split("|")
        for e in entry.tags:
            for s in kw:
                    if s == e:
                        return True
        return False
    else:
        return search in entry.tags

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
        search_term = ""
        while(search_term == ''):
                search_term = input("Search for (q for exit): ")
                if search_term == "":
                    print("Please provide a search term\n")
        if search_term == "q":
            print("Bye")
            break
        filtered_results = [e for e in entries if filter_entries_by_tag(search_term,e)]
        filtered_results = sorted(filtered_results, key=attrgetter("date"))
        n = len(filtered_results)
        
        for e in filtered_results:
            print(f"{e.date} | {e.title}")
        if n == 0:
            print(f'\n0 entries matched "{search_term}"\n')
        if n == 1:
            print(f'\n1 entry matched "{search_term}"\n')
        elif n > 1:
            print(f'\n{n} entries matched "{search_term}"\n')


if __name__ == '__main__':
    main()
