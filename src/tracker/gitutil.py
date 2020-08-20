import re


def find_tag(repo, pattern):
    """Find tag that matches the given regex pattern in the repository.

    Args:
        repo (Repo): A Repo object
        pattern (string): regex pattern to match

    Returns:
        TagReference: A reference to the first occurred tag
                      that matches `pattern`
    """
    p = re.compile(pattern)
    return next((x for x in repo.tags if p.match(x.name)), None)
