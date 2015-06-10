__author__ = 'seven'
"""
This code combines the output of the tokeniser and the input tweet set and
returns the final input file in the following format:
tweet Id, Tweet tokens, POS tokens,label
"""

import sys
from itertools import izip


def combine():
    """check arguments"""
    if len(sys.argv) != 4:
        print "Usage :: python combine.py " \
              "./SemEval2014-task9-test-B-gold_reformated " \
              "./tweetsTagged.txt " \
              "./SemEval2014_test.csv"
        sys.exit(0)

    """Parallely combine both the files"""
    print ("Combine and create SemEval2014_test.csv")
    data = []
    infile1 = open(sys.argv[1], 'r')
    infile2 = open(sys.argv[2], 'r')
    for line1, line2 in izip(infile1, infile2):
        tmp1 = line1.strip().split('\t')
        tmp2 = line2.strip().split('\t')
        string = tmp1[0] + '\t' + tmp2[0] + '\t' + \
            tmp2[1] + '\t' + tmp1[2] + '\n'
        data.append(string)
    infile1.close()
    infile2.close()

    """write into file"""
    outfile = open(sys.argv[3], 'w')
    outfile.write("".join(data))
    outfile.close()


if __name__ == "__main__":
    combine()