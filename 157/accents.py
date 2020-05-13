from unicodedata import decomposition


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return [chr for chr in text.lower() if decomposition(chr)]