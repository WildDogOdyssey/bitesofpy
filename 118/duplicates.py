from collections import Counter


def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    # words = list(map(lambda word: word.lower(), words))
    # word_count = Counter(words)
    # repeated = dict(filter(lambda x: x[1] > 1, word_count.items()))
    # return [words.index(word) for word in repeated.keys()]

    repeated = set(word for word in words if words.count(word) > 1)
    return [words.index(word) for word in repeated]

words = ['is', 'it', 'true', 'or', 'is', 'it', 'not']
print(get_duplicate_indices(words))