import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
#urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    words = set(_get_permutations_draw(draw))
    return list(words & dictionary)

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    result = list()
    draw = list(set(draw))
    for n in range(1, len(draw)+1):
        perms = itertools.permutations(draw, n) 
        for p in perms:
            p_lower = [w.lower() for w in p]
            word = ''.join(p_lower)
            result.append(word)
    return result

if __name__ == '__main__':
    letters = 'O, N, V, R, A, Z, H'.split(', ')
    print(get_possible_dict_words(letters))


