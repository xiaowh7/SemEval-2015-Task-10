from itertools import izip

__author__ = 'seven'


def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        print 'Create directory ' + path
        os.makedirs(path)
        return True
    else:
        print 'Directory ' + path + ' already exists'
        return False


if __name__ == '__main__':
    reformattedFilename = "SemEval2014-task9-test-B-gold_reformated.txt"
    testFilename = "SemEval2014_test.csv"
    dependencyFilename = "SemEval2014_test_dependency.txt"

    reformattedFile = open(reformattedFilename, 'r')
    reformattedLines = reformattedFile.readlines()
    reformattedFile.close()

    testFile = open(testFilename, 'r')
    testLines = testFile.readlines()
    testFile.close()

    dependencyFile = open(dependencyFilename, 'r')
    dependencyLines = dependencyFile.readlines()
    dependencyFile.close()

    dirAbbrDict = {"Twitter-2013": "T13", "SMS-2013": "SM",
                   "Twitter-2014": "T14", "Twitter-2014-sracasm": "TS",
                   "LiveJournal-2014": "LJ"}

    for dirName in dirAbbrDict.keys():
        mkdir(dirName)
        outputGoldFilename = "%s//%s_gold.csv" % (dirName, dirName)
        outputGoldFile = open(outputGoldFilename, 'w')
        outputTestFilename = "%s//%s_test.csv" % (dirName, dirName)
        outputTestFile = open(outputTestFilename, 'w')
        outputDepFilename = "%s//%s_dependency.txt" % (dirName, dirName)
        outputDepFile = open(outputDepFilename, 'w')

        for i in xrange(len(reformattedLines)):
            reformattedLine = reformattedLines[i]
            testLine = testLines[i]
            dependencyLine = dependencyLines[i]

            data = reformattedLine.strip("\r\n").split("\t")
            source = data[1]
            content = data[3]
            if source.startswith(dirAbbrDict[dirName]) and \
                    not content == "Not Available":
                outputGoldFile.write(reformattedLine)
                outputTestFile.write(testLine)
                outputDepFile.write(dependencyLine)

        outputGoldFile.close()

    reformattedFile.close()
    # exit(0)



    # for line1, line2, line3 in \
    #         izip(reformattedFile, goldFile, dependencyFilename):
    #     data1 = line1.strip('\r\n').split('\t')
    #     source = data1[1]
    #     if not (source.startswith("SM") or source.startswith("T13")
    #             or source.startswith("T14") or source.startswith("LJ")):
    #         print source