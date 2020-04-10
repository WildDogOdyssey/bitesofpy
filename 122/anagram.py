def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1_lst = sorted([ch for ch in word1.lower() if ch.isalnum()])
    word2_lst = sorted([ch for ch in word2.lower() if ch.isalnum()])

    if word1_lst == word2_lst:
        return True
    else:
        return False

# print(is_anagram("rail safety", "fairy tales"))