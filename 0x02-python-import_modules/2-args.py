#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    tal = len(sys.argv)
    if tal == 1:
        print("{} arguments.".format(tal - 1))
    elif tal == 2:
        print("{} argument:".format(tal - 1))
    else:
        print("{} arguments:".format(tal - 1))

    for i in range(1, tal):
        print("{}: {}".format(i, sys.argv[i]))

