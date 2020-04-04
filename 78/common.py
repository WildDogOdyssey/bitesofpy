def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    # lang_set = {language for programmer in programmers.values() for language in programmer}
    # for language in programmers.values():
    #     lang_set = lang_set.intersection(language)
    # return lang_set

    return set.intersection(*(set(languages) for languages in programmers.values()))