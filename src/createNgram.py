__author__ = 'seven'
from replaceExpand import *
import sys


def output(gramDict, outfileName, threshold):
    gramList = []
    for i in gramDict.keys():
        count = reduce(lambda x, y: x + y, gramDict[i])
        if count >= 5:
            count *= 1.0
            pos = gramDict[i][positive] / count
            neg = gramDict[i][negative] / count
            neu = gramDict[i][neutral] / count
            if pos > threshold or neg > threshold or neu > threshold:
                l = [i, pos, neg, neu, count]
                gramList.append(l)
    gramList = sorted(gramList, key=lambda x: x[4], reverse=True)
    outfile = open(outfileName, 'w')
    for i in xrange(len(gramList)):
        if i > 0:
            outfile.write('\n')
        outfile.write("%s" % gramList[i][0])


def createChargram(dataset, seqLen=3, threshold=0.8):
    if dataset == "Semeval" or dataset == "SemEval" or \
        dataset == "semeval":
        infileName = "../dataset/trainset/train.csv"
        outfileName = \
            "../requirement/ngram/Semeval/Semeval_%dChargram.txt" % seqLen
    elif dataset == "Semeval-dev" or dataset == "SemEval-dev" or \
        dataset == "semeval-dev":
        infileName = "../dataset/trainset/train_full.csv"
        outfileName = \
            "../requirement/ngram/Semeval-dev/Semeval-dev_%dChargram.txt" \
            % seqLen
    elif dataset == "Real-time":
        infileName = "../dataset/Real-time/Real-time_train.csv"
        outfileName = \
            "../requirement/ngram/Real-time/Real-time_%dChargram.txt" % seqLen
    else:
        exit("Error: Wrong dataset\nPlease specify a valid dataset.")

    chargramDict = {}
    infile = open(infileName, 'r')
    for line in infile:
        if line:
            line = line.strip('\n').split('\t')
            tokens = line[1].split()
            label = line[3].strip()
            if tokens and line[1] != "Not Available":
                tokens = [i.strip(specialChar).lower() for i in tokens]
                tokens = [i for i in tokens if i]
                for token in tokens:
                    if len(token) > 3:
                        for i in xrange(len(token) - 2):
                            seq = token[i:i + seqLen]
                            if seq not in chargramDict:
                                chargramDict[seq] = [0, 0, 0]
                            chargramDict[seq][eval(label)] += 1

    infile.close()

    output(chargramDict, outfileName, threshold)


def createNgram(dataset, phraseLen, threshold=0.8):
    if phraseLen == 1:
        feature = "uni"
    elif phraseLen == 2:
        feature = "bi"
    elif phraseLen == 3:
        feature = "tri"
    elif phraseLen == 4:
        feature = "4"
    else:
        exit("Error: Wrong value for phrase length\n"
             "Please specify a valid n for ngram.")

    if dataset == "Semeval" or dataset == "SemEval" or \
        dataset == "semeval":
        infileName = "../dataset/trainset/train.csv"
        outfileName = \
            "../requirement/ngram/Semeval/Semeval_%sgram.txt" % feature
    elif dataset == "Semeval-dev" or dataset == "SemEval-dev" or \
        dataset == "semeval-dev":
        infileName = "../dataset/trainset/train_full.csv"
        outfileName = \
            "../requirement/ngram/Semeval-dev/Semeval-dev_%sgram.txt" % feature
    elif dataset == "Real-time":
        infileName = "../dataset/Real-time/Real-time_train.csv"
        outfileName = \
            "../requirement/ngram/Real-time/Real-time_%sgram.txt" % feature
    else:
        exit("Error: Wrong dataset\nPlease specify a valid dataset.")

    ngramDict = {}
    infile = open(infileName, 'r')
    for line in infile:
        if line:
            line = line.strip('\n').split('\t')
            tokens = line[1].split()
            label = line[3].strip()
            if tokens and line[1] != "Not Available":
                tokens = [i.strip(specialChar).lower() for i in tokens]
                tokens = [i for i in tokens if i]

                if phraseLen == 1:
                    for i in range(len(tokens)):
                        phrase = tokens[i]
                        if phrase not in ngramDict:
                            ngramDict[phrase] = [0, 0, 0]
                        ngramDict[phrase][eval(label)] += 1
                elif phraseLen == 2:
                    for i in range(len(tokens) - 1):
                        phrase = tokens[i] + ' ' + tokens[i + 1]
                        if phrase not in ngramDict:
                            ngramDict[phrase] = [0, 0, 0]
                        ngramDict[phrase][eval(label)] += 1
                elif phraseLen == 3:
                    for i in range(len(tokens) - 2):
                        phrase = tokens[i] + ' ' + tokens[i + 1] + ' ' + \
                            tokens[i + 2]
                        if phrase not in ngramDict:
                            ngramDict[phrase] = [0, 0, 0]
                        ngramDict[phrase][eval(label)] += 1

                        phrase = tokens[i] + ' ' + '*' + ' ' + tokens[i + 2]
                        if phrase not in ngramDict:
                            ngramDict[phrase] = [0, 0, 0]
                        ngramDict[phrase][eval(label)] += 1
                elif phraseLen == 4:
                    for i in range(len(tokens) - 3):
                        phrase = tokens[i] + ' ' + tokens[i+1] + ' ' + \
                            tokens[i+2] + ' ' + tokens[i+3]
                        if phrase not in ngramDict:
                            ngramDict[phrase] = [0, 0, 0]
                        ngramDict[phrase][eval(label)] += 1

                        phrase = tokens[i] + ' ' + '*' + ' ' + \
                            tokens[i+2] + ' ' + tokens[i+3]
                        if phrase not in ngramDict:
                            ngramDict[phrase] = [0, 0, 0]
                        ngramDict[phrase][eval(label)] += 1

                        phrase = tokens[i] + ' ' + tokens[i+1] + ' ' + \
                            '*' + ' ' + tokens[i+3]
                        if phrase not in ngramDict:
                            ngramDict[phrase] = [0, 0, 0]
                        ngramDict[phrase][eval(label)] += 1
                else:
                    exit("Error: Wrong value for phrase length\n"
                         "Please specify a valid n for ngram.")

    infile.close()

    output(ngramDict, outfileName, threshold)


if __name__ == "__main__":
    dataset = sys.argv[1]
    print "Creating %s_3Chargram.txt..." % dataset
    createChargram(dataset, 3, 0.7)
    print "Creating %s_4Chargram.txt..." % dataset
    createChargram(dataset, 4, 0.7)
    print "Creating %s_5Chargram.txt..." % dataset
    createChargram(dataset, 5, 0.7)

    print "Creating %s_unigram.txt..." % dataset
    createNgram(dataset, 1, 0.6)
    print "Creating %s_bigram.txt..." % dataset
    createNgram(dataset, 2, 0.6)
    print "Creating %s_trigram.txt..." % dataset
    createNgram(dataset, 3, 0.6)
    print "Creating %s_4gram.txt..." % dataset
    createNgram(dataset, 4, 0.6)

    print "%s ngram created." % dataset
