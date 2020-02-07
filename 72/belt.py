from collections import OrderedDict
from itertools import takewhile
# from pprint import pprint as pp

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
# =============================================================================
#     for score in reversed(scores):
#         if score <= user_score:
#             return HONORS.get(score)
# =============================================================================
    try: 
        return HONORS.get(max(takewhile(lambda s: s <= user_score, scores)))
    except:
        return None
