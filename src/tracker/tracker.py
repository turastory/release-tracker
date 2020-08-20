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
from tracker import meta


def func(x):
    return x + 1


if __name__ == "__main__":
    arguments = docopt(__doc__, version=meta.__version__)
    print(arguments)
