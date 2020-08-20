import os
import pytest
import git
from tracker import gitutil


def setup_git_repo(repo_dir):
    return git.Repo.init(repo_dir)


def commit_new_file(repo, name, message="test commit"):
    filename = os.path.join(repo.working_dir, name)
    open(filename, "wb").close()
    repo.index.add([filename])
    repo.index.commit(message)


def test_get_name_from_tag_path():
    assert gitutil.get_name_from_tag_path("refs/tags/test") == "test"


def test_get_name_from_tag_path_invalid_input():
    with pytest.raises(AssertionError):
        gitutil.get_name_from_tag_path("invalid")


def test_find_tag(tmpdir):
    repo = setup_git_repo(tmpdir)
    commit_new_file(repo, "first", "Initial Commit")
    repo.create_tag("test")
    commit_new_file(repo, "second")
    repo.create_tag("abcd")
    assert gitutil.find_tag(repo, "test") == "test"
    assert gitutil.find_tag(repo, "a.*") == "abcd"
