import inspect


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [mem[0] for mem in inspect.getmembers(mod)
            if inspect.isclass(mem[1]) and mem[0][0].isupper()]