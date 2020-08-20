import re
from git import Repo


def get_name_from_tag_path(path):
    tag_prefix = "refs/tags/"
    assert path.startswith(tag_prefix)
    return path[len(tag_prefix):]


def find_tag(repo_path, pattern):
    repo = Repo(repo_path)
    p = re.compile(pattern)
    tag_names = map(lambda x: get_name_from_tag_path(x.path), repo.tags)
    return next((x for x in tag_names if p.match(pattern)), None)
