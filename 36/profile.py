def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError
    res = {'name': name, 'age': age}
    if sports:
        if len(sports) > 5:
            raise ValueError
        else:
            res['sports'] = sorted(sports)
    if awards:
        res['awards'] = dict(**awards)
    return res