import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    mo = re.findall(r'\w[^\.\?!]+[\.\?!]', text)
    return ' '.join(line[0].upper() + line[1:] for line in mo)