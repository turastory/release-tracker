"""
Test document.

Usage:
  track <start> [<target>] [--regex=<regex>] [--dir=<dir>]
  track (-h | --help)
  track --version

Options:
  -h --help           Show this screen.
  --version           Show version.
  -r, --regex=<regex> Regular expression to filter out commits
  -d, --dir=<dir>     Target directory.

"""
from docopt import docopt
try:
    from tracker import meta
except Exception:
    import meta


if __name__ == "__main__":
    arguments = docopt(__doc__, version=meta.__version__)
    print(arguments)
