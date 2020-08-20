import re
from git import Repo


def get_name_from_tag_path(path):
    """Get only the name from the given path of the tag.
    If the given path doesn't match the format of the git tag,
    raise AssertionError.
    """
    tag_prefix = "refs/tags/"
    assert path.startswith(tag_prefix)
    return path[len(tag_prefix):]


def find_tag(repo_path, pattern):
    """Find tag that matches the given regex pattern in the repository.

    Args:
        repo_path (string): A path pointing to the repository
        pattern (string): regex pattern to match

    Returns:
        string: Name of the first occurred tag that matches `pattern`
    """
    repo = Repo(repo_path)
    p = re.compile(pattern)
    tag_names = map(lambda x: get_name_from_tag_path(x.path), repo.tags)
    return next((x for x in tag_names if p.match(pattern)), None)
