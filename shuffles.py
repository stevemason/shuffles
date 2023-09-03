"""Shuffles Spotify playlist properly."""
from sys import argv, exit

from init import reinitialize
from init import user_auth
from playlist import shuffle

args = argv[1:]  # command line args


def usage():
    """Display usage and exit."""
    print()
    print("Usage:")
    print()
    print("shuffles.py --auth")
    print("shuffles.py --code *authorisation code*")
    print("shuffles.py --playlist *playlist ID*")
    print()
    exit(-1)


if len(args) == 1:
    arg = args[0].lower()
    if arg == "-a" or arg == "--auth":
        user_auth()
        exit(0)

if len(args) != 2:
    usage()

arg = args[0].lower()

if arg == "-p" or arg == "--playlist":
    playlist = args[1]
    shuffle(playlist)
elif arg == "-c" or arg == "--code":
    code = args[1]
    reinitialize(code)
else:
    usage()

exit(0)
