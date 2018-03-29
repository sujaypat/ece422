#!/usr/bin/python2.7
import dpkt
import sys


def main():
    if (len(sys.argv) < 2):
        print "error: need argument"
        sys.exit(1)

    filename = sys.argv[1]
    print "input filename: " + filename
    print "fixme"
    sys.exit(0)


if __name__ == '__main__':
    main()
