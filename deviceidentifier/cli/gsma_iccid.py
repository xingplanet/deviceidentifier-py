#!/usr/bin/env python
from deviceidentifier import api

import sys, json


def main():
    # Sample showing how to look up data from a GSMA ICCID.

    if len(sys.argv) < 2:
        print 'Usage: provide a GSMA ICCID for a breakdown of data on it.'
        exit(-1)

    print json.dumps( api.lookup( api.TYPE_GSMA_ICCID, sys.argv[1:][0] ), indent=4 )

if __name__ == '__main__':
    main()
