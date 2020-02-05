import itertools
import os
import urllib.request

# remember to release this before submission
# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

# =============================================================================
# # remember to delete or comment this before submission
# with open('dictionary.txt', 'r') as f:
#     dictionary = set([word.strip().lower() for word in f.read().split()])
# =============================================================================


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    
    permu_set = set(_get_permutations_draw(draw))
    
    return permu_set & dictionary

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw = [ch.lower() for ch in draw]
    
    permu = []
    
    for i in range(len(draw)):
        permu = permu + [''.join(line) for line in itertools.permutations(draw, i)]
    
    return permu

# print(dictionary)
# test1 = 'T, I, I, G, T, T, L'.split(', ')
# test2 = 'O, N, V, R, A, Z, H'.split(', ')
# print(test2)
# print(_get_permutations_draw(test2))
# print(get_possible_dict_words(test1))