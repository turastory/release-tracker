import re


def find_tag(repo, pattern):
    """Find tag that matches the given regex pattern in the repository.

    Args:
        repo (Repo): A Repo object
        pattern (string): regex pattern to match

    Returns:
        string: Name of the first occurred tag that matches `pattern`
    """
    p = re.compile(pattern)
    tag_names = map(lambda x: x.name, repo.tags)
    return next((x for x in tag_names if p.match(x)), None)
