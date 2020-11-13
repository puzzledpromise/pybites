from collections import Counter, defaultdict
from operator import itemgetter
import csv
import re
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    season_data = content.split('\n')[1:]
    character_dict = dict()
    for l in season_data:
        l = l.replace('"',"")
        re.sub('\d*,\d*',)
        if not l == "":
            if l[0].isdigit():
                l = l.replace("0,0","00")
                parts = l.split(',')
                s = parts.pop(0)
                e = parts.pop(0)
                actor = parts.pop(0)

                if actor not in character_dict:
                    character_dict[actor] = dict()
                if e not in character_dict[actor]:
                    character_dict[actor][e] = 0
                parts = [p.split(" ") for p in parts]
            else:
                parts = l.split(" ")
        else:
            continue

        words = list()

        for p in parts:
            if isinstance(p,list):
                words.extend(p)
            else:
                words.append(p)
            words = [w for w in words if w != ""]
        character_dict[actor][e] = character_dict[actor][e] + len(words)
    result = dict()
    for c in character_dict.keys():
        result[c] = Counter(character_dict[c])

    return result

if __name__ == "__main__":
    season_content = get_season_csv_file(5)
    num_words = get_num_words_spoken_by_character_per_episode(season_content)
    print(num_words["Ms. Choksondik"])

