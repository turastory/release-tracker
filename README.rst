Release Tracker V2
==================

The purpose
-----------

After switching to use tags rather release commits for deployment, It becomes hard to track what've changed since the last release.

This simple utility examines git logs and show the list of commits that are added after certain tag.


How to use
------------

Usage:
  `track <start-tag-name> [target-tag-name]`

Note that you should run inside another git repository. (Perhaps the one that you are working on)

How it works
------------

#. Search for the given pattern in the existing tags.
#. From there, collect all commits that matches specific patterns, from older to newer.
