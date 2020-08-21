Release Tracker V2 (No future updates)
==================

While examining git and gitpython, I noticed that **the desired behavior already exists in Git!**
Here's a simple example:

```bash
$ git log HEAD...some/tag/name/3 --oneline --decorated --grep="pattern"
```

There's no reason to reinvent the wheel, so **I decided not to work on it anymore.**


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


How to build
------------

.. code:: bash

    # Set up a virtual environment.
    $ virtualenv venv
    $ . venv/bin/activate
    
    # Install the dependencies
    $ pip install -r requirements.txt

    # To run tests:
    $ tox

