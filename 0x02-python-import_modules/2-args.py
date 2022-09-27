#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    tal = len(sys.argv) - 1
    if tal == 0:
        print("0 arguments.")
    elif tal == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(tal))

    for i in range(tal):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
