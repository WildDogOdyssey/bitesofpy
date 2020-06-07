def flatten(list_of_lists):
    lst = []
    for n in list_of_lists:
        if isinstance(n, (list, tuple)):
            lst += flatten(n)
        else:
            lst.append(n)
    return lst

# test = [1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
# print(flatten(test))