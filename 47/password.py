import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):

    digits, lowers, uppers, punc = [int(d) for d in '0000']
    used = password not in used_passwords
    leng = len(password)
    length = (leng > 5 and leng < 13)

    for w in password:
        if w.isdigit():
            digits += 1
        elif w.islower():
            lowers += 1
        elif w.isupper():
            uppers += 1
        elif w in PUNCTUATION_CHARS:
            punc += 1

    if all([used, length,
        digits > 0,
        lowers > 1,
        uppers > 0,
        punc > 0
    ]):
        used_passwords.add(password)
        return True
    else:
        return False

    # ops_dict = dict(zip([str.isalpha, str.islower, str.isupper], [1, 2, 1]))
    #
    # res = True
    # length = len(password)
    # if password in used_passwords:
    #     res = False
    # elif length < 6 or length > 12:
    #     res = False
    #
    # for f, v in ops_dict.items():
    #     if sum([f(w) for w in password]) < v:
    #         res = False
    #
    # if sum([True for w in password if w in PUNCTUATION_CHARS]) < 1:
    #     res = False
    #
    # if res:
    #     used_passwords.add(password)
    # return res

# print(validate_password('PyBites@1912'))