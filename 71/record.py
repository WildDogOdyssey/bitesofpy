class RecordScore():
    """Class to track a game's maximum score"""

    # highest_score = None
    #
    # def __call__(self, score):
    #     if self.highest_score == None:
    #         self.highest_score = score
    #     elif score > self.highest_score:
    #         self.highest_score = score
    #     return self.highest_score

    def __init__(self):
        self.highest_score = float('-inf')

    def __call__(self, score):
        if self.highest_score < score:
            self.highest_score = score
        return self.highest_score

record = RecordScore()  # init
print(record(10))  # call
print(record(9))
print(record(11))
record = RecordScore()
print(record(-2))
print(record(-1))
