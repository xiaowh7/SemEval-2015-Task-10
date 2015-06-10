import re

__author__ = 'seven'
def Semeval2014Output(predictLabel, goldFilename, predFilename):
    goldFile = open(goldFilename, 'r')
    predFile = open(predFilename, 'w')

    index = 0
    for line in goldFile:
        data = line.strip("\r\n").split("\t")
        predFile.write("%s\t%s\t%s\n" % (data[0], data[1], predictLabel[index]))
        index += 1

    goldFile.close()
    predFile.close()


def Semeval2013Output(predictLabel, goldFilename, predFilename):
    goldFile = open(goldFilename, 'r')
    predFile = open(predFilename, 'w')

    index = 0
    for line in goldFile:
        data = line.strip("\r\n").split("\t")
        predFile.write("%s\t%s\t%s\t%s\n" %
                       (data[0], data[1], predictLabel[index], data[3]))
        index += 1

    goldFile.close()
    predFile.close()


def output(dataset, addTrainsetList, goldFilename, predictLabel):
    datasetList = [dataset]
    if not len(addTrainsetList) == 0:
        for addTrainset in addTrainsetList:
            datasetList.append(addTrainset)
    filenamePrefix = "_".join(datasetList)
    if dataset.startswith("Twitter") or dataset.startswith("twitter"):
        year = re.findall(r'\d+', dataset)[0]
        predFilename = \
                "../dataset/SemEval2014-Task9/Twitter-%s/%s_pred.csv" \
                % (year, filenamePrefix)
        Semeval2013Output(predictLabel, goldFilename, predFilename)
    elif dataset == "Semeval2013" or dataset == "SemEval2013" or \
                    dataset == "semeval2013":
        predFilename = \
                "../dataset/SemEval2013-Task2B/tweet/%s_pred.csv" % \
                filenamePrefix
        Semeval2013Output(predictLabel, goldFilename, predFilename)
    elif dataset == "Real-time":
        predFilename = "../dataset/%s/%s_pred.csv" % (dataset, filenamePrefix)
        Semeval2013Output(predictLabel, goldFilename, predFilename)
    else:
        predFilename = "../result/%s.pred" % filenamePrefix
        Semeval2014Output(predictLabel, goldFilename, predFilename)