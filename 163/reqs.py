def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old, new = _parse(old_reqs), _parse(new_reqs)
    ver_dict = dict(zip(new.keys(), zip(old.values(), new.values())))
    return [pkg for pkg, vers in ver_dict.items()
            if _cal_version_score(vers[0]) < _cal_version_score(vers[1])]
#     return [pkg for pkg, vers in new_dict.items() if _compare_ver(vers)]
#
# def _compare_ver(vers: tuple) -> bool:
#     "Split the version string by '.' and compare values in each segment"
#     pairs = zip(vers[0].split('.'), vers[1].split('.'))
#     for i in pairs:
#         if int(i[0]) > int(i[1]):
#             return False
#         elif int(i[0]) == int(i[1]):
#             continue
#         else:
#             return True

def _cal_version_score(ver: str) -> int:
    "Helper function to calculate a score for package version. Assuming maximum two digits for each segment."
    a, b, *c = iter(int(d) for d in ver.split('.'))
    return sum([a*10000, b*100, *c])

def _parse(reqs: str) -> dict:
    """Helper function to parse a multi-line string requirement into a dictionary
       with packages as keys and versions as values
    """
    return {line.split('==')[0]:line.split('==')[1]
            for line in reqs.strip().splitlines()}