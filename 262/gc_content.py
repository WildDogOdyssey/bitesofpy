from collections import Counter

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    c = Counter(sequence.lower())
    gc = c['g'] + c['c']
    total = gc + c['a'] + c['t']
    return round(gc * 100 / total, 2)

