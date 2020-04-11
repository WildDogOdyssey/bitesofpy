import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    mo = re.findall(r'\w[^\.\?!]+[\.\?!]', text)
    return ' '.join(line.capitalize() for line in mo)