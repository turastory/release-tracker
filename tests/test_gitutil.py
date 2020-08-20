import os
import pytest
import git
from tracker import gitutil


def test_get_name_from_tag_path():
    assert gitutil.get_name_from_tag_path("refs/tags/test") == "test"


def test_get_name_from_tag_path_invalid_input():
    with pytest.raises(AssertionError):
        gitutil.get_name_from_tag_path("invalid")


def setup_git_repo(repo_dir):
    file_name = os.path.join(repo_dir, 'new-file')
    r = git.Repo.init(repo_dir)
    open(file_name, 'wb').close()
    r.index.add([file_name])
    r.index.commit("Initial commit")
    return r


def test_find_tag(tmpdir):
    repo = setup_git_repo(tmpdir)
    repo.create_tag("test")
    assert gitutil.find_tag(repo, "test") == "test"
