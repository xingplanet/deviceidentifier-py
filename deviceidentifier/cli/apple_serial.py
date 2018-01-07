#!/usr/bin/env python
from deviceidentifier import api

import sys, json


def main():
    # Sample showing how to look up data from an Apple serial.

    if len(sys.argv) < 2:
        print 'Usage: provide an Apple serial for a breakdown of data on it.'
        exit(-1)

    print json.dumps( api.lookup( api.TYPE_APPLE_SERIAL, sys.argv[1:][0] ), indent=4 )

if __name__ == '__main__':
    main()
