from difflib import SequenceMatcher
import os
from urllib.request import urlretrieve
import requests

# TMP = os.getenv("TMP", "/tmp")
# DICTIONARY = os.path.join(TMP, 'dictionary.txt')
# if not os.path.isfile(DICTIONARY):
#     urlretrieve(
#         'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
#         DICTIONARY
#     )

r = requests.get('https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt')
DICTIONARY = r.text.strip().split('\n')

def load_words():
    'return dict of words in DICTIONARY'
    # with open(DICTIONARY) as f:
    #     return {word.strip().lower() for word in f.readlines()}
    return {word.strip().lower() for word in DICTIONARY}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    checker = SequenceMatcher()
    checker.set_seq1(misspelled_word)

    # matches = []
    # for idx, word in enumerate(words):
    #     checker.set_seq2(word)
    #     matches.append((idx, checker.ratio()))
    #
    # best_match_idx = max(matches, key=lambda x: x[1])[0]
    # return list(words)[best_match_idx]

    suggest = None
    max_ratio = 0
    for word in words:
        checker.set_seq2(word)
        ratio = checker.ratio()
        if ratio > max_ratio:
            suggest = word
            max_ratio = ratio

    return suggest

# print(suggest_word('prfomnc'))