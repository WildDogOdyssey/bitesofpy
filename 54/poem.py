import textwrap


INDENTS = 4


def print_hanging_indents(poem):
    wrapper = textwrap.TextWrapper(width=50, initial_indent='', subsequent_indent=' '*INDENTS)

    for block in poem.strip().split('\n\n'):
        print(wrapper.fill(block.strip()))

# rosetti_unformatted = """
#                       Remember me when I am gone away,
#                       Gone far away into the silent land;
#                       When you can no more hold me by the hand,
#
#                       Nor I half turn to go yet turning stay.
#
#                       Remember me when no more day by day
#                       You tell me of our future that you planned:
#                       Only remember me; you understand
#                       """
#
# print_hanging_indents(rosetti_unformatted)