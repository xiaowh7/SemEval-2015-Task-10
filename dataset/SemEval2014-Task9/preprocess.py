from itertools import izip

__author__ = 'seven'
import sys
import re


def reformat():
    if len(sys.argv) != 4:
        print "Usage :: python preprocess.py " \
              "InputFileName ReformatFileName OutputFileName"
        sys.exit(0)

    print ("Reformatting...")
    originFilename = "SemEval2014-Task9-subtaskAB-test-to-download/" \
                     "SemEval2015-task10-test-B-input-progress.txt"
    originFile = open(originFilename, 'r')

    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')


    for line1, line2 in izip(infile, originFile):
        index = line1.split('\t')[0]
        source = line1.split('\t')[1]
        sentiment = line1.split('\t')[2]
        content = line2.strip('\r\n').split('\tunknwn\t')[1]
        outfile.write("%s\t%s\t%s\t%s\n" % (index, source, sentiment, content))


def extractContent():
    p = re.compile("\\t(neutral|positive|negative)\\t.*$")

    print ("Extracting tweets...")
    infile = open(sys.argv[2], 'r')
    outfile = open(sys.argv[3], 'w')

    for line in infile:
        regs = p.search(line).regs
        start = regs[1][1] + 1
        end = regs[0][1]
        content = line[start:end]
        content = content.replace('\t', ' ')
        outfile.write("%s\n" % content)


if __name__ == "__main__":
    reformat()
    extractContent()