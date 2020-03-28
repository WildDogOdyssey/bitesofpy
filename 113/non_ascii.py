import string


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    ascii_printables = set(string.printable)
    return [word for word in text.split() if len(set(word).difference(ascii_printables)) > 0]