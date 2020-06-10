def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    left_of_quote, _, remains = text.partition('"')
    quote, _, right_of_quote = remains.rpartition('"')
    return left_of_quote.split() + [quote] + right_of_quote.split()

# test = 'Our first program was "Hello PyBites"'
# print(split_words_and_quoted_text(test))