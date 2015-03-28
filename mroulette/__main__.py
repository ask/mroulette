import sys

from mroulette import mroulette


def main(*args, **kwargs):
    sys.exit(mroulette().execute_from_commandline(*args, **kwargs))


if __name__ == '__main__':
    main()
