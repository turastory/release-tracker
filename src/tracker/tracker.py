"""
Test document.

Usage:
  track <start-tag-name> [<target-tag-name>]
  track (-h | --help)
  track --version

Options:
  -h --help       Show this screen.
  --version       Show version.
  --regex=<regex> Regular expression to filter out commits

"""
from docopt import docopt


def func(x):
    return x + 1


if __name__ == "__main__":
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)
