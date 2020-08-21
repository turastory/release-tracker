import re


def filter_regex(strings, pattern):
    """Filter out the given list of strings
    using regex with the given pattern.
    """
    p = re.compile(pattern)
    return list(filter(lambda x: p.match(x), strings))
