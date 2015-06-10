from itertools import izip

__author__ = 'seven'
import sys
import re


def extractContent():
    if len(sys.argv) != 3:
        print "Usage :: python preprocess.py " \
              "InputFileName OutputFileName"

    print ("Extracting tweets...")
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')

    for line in infile:
        content = line.strip('\r\n').split('\tunknwn\t')[1]
        # print content
        # regs = p.search(line).regs
        # start = regs[1][1] + 1
        # end = regs[0][1]
        # content = line[start:end]
        # content = content.replace('\t', ' ')
        outfile.write("%s\n" % content)

    infile.close()
    outfile.close()


if __name__ == "__main__":
    extractContent()