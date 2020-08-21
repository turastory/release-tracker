import os
import git
from tracker import gitutil


def setup_git_repo(repo_dir):
    return git.Repo.init(repo_dir)


def commit_new_file(repo, name, message="test commit"):
    filename = os.path.join(repo.working_dir, name)
    open(filename, "wb").close()
    repo.index.add([filename])
    repo.index.commit(message)


def test_find_tag(tmpdir):
    repo = setup_git_repo(tmpdir)
    commit_new_file(repo, "first", "Initial Commit")
    repo.create_tag("test")
    commit_new_file(repo, "second")
    repo.create_tag("abcd")
    assert gitutil.find_tag(repo, "test").name == "test"
    assert gitutil.find_tag(repo, "a.*").name == "abcd"


def test_list_commits(tmpdir):
    repo = setup_git_repo(tmpdir)
    commit_new_file(repo, "first", "first commit")
    tag1 = repo.create_tag("first_tag")
    commit_new_file(repo, "second", "second commit")
    tag2 = repo.create_tag("second_tag")
    commit_new_file(repo, "third", "third commit")
    assert [x.message
            for x
            in gitutil.list_commits(repo, "HEAD", tag1.path)
            ] == ["third commit", "second commit"]
    assert [x.message
            for x
            in gitutil.list_commits(repo, "HEAD", tag2.path)
            ] == ["third commit"]
