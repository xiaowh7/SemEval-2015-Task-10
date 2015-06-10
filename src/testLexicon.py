import sys
from prepare import *


def calculateLexiconScore(lexiconDict, goldFilename):
    index = 0
    posBingo = 0
    negBingo = 0
    posCount = 0
    negCount = 0
    posPredict = 0
    negPredict = 0

    inFile = open(goldFilename, 'r')
    for line in inFile:
        if line:
            index += 1
            # print line
            line = line.strip('\n').split('\t')
            tokens = line[1].split()
            label = line[3].strip()

            total = 0
            if tokens and not label == 'neutral':
                tokens = [i for i in tokens if i]
                # unigram score
                for i in range(len(tokens)):
                    phrase = tokens[i]
                    phrase = phrase.lower()
                    if phrase in lexiconDict:
                        total += lexiconDict[phrase]

                # print "Index: %d, Total Score: %f, Label: %s" % (
                # index, total, label)

                if label == 'positive':
                    posCount += 1
                elif label == 'negative':
                    negCount += 1

                if total > 0:
                    posPredict += 1
                    if label == 'positive':
                        posBingo += 1
                elif total < 0:
                    negPredict += 1
                    if label == 'negative':
                        negBingo += 1
    inFile.close()
    return negCount, negBingo, negPredict, posCount, posBingo, posPredict


def testLexiconOutput(
        negCount, negBingo, negPredict, posCount, posBingo, posPredict):
    print "For positive labels:"
    print "Bingo: %d, TotalPosPredict: %d, TotalPositive: %d" % \
          (posBingo, posPredict, posCount)
    print "Precision: %f, Recall: %f, " % \
          (float(posBingo) / posPredict, float(posBingo) / posCount)

    print "For negative labels:"
    print "Bingo: %d, TotalNegPredict: %d, TotalNegative: %d" % \
          (negBingo, negPredict, negCount)
    print "Precision: %f, Recall: %f " % \
          (float(negBingo) / negPredict, float(negBingo) / negCount)


def testLiuBingLexicon(goldFilename):
    print "\nTesting LiuBing lexicon..."
    LiuBingLexicon = loadLiuBingLexicon()
    negCount, negBingo, negPredict, posCount, posBingo, posPredict = \
        calculateLexiconScore(LiuBingLexicon, goldFilename)
    testLexiconOutput(
        negCount, negBingo, negPredict, posCount, posBingo, posPredict)


def testMPQALexicon(goldFilename):
    print "\nTesting MPQA lexicon..."
    MPQALexicon = loadMPQALexicon()
    negCount, negBingo, negPredict, posCount, posBingo, posPredict = \
        calculateLexiconScore(MPQALexicon, goldFilename)
    testLexiconOutput(
        negCount, negBingo, negPredict, posCount, posBingo, posPredict)


def testNRCEmotionLexicon(goldFilename):
    print "\nTesting NRCEmotion lexicon..."
    NRCEmotionLexicon = loadNRCEmoticonLexicon()
    negCount, negBingo, negPredict, posCount, posBingo, posPredict = \
        calculateLexiconScore(NRCEmotionLexicon, goldFilename)
    testLexiconOutput(
        negCount, negBingo, negPredict, posCount, posBingo, posPredict)


def testNRCCanadaLexicon(src, goldFilename):
    print "\nTesting NRC-Canada %s lexicon..." % src
    unigram, bigram, pairs = loanNRCCanadaLexicon(src)
    negCount, negBingo, negPredict, posCount, posBingo, posPredict = \
        calculateLexiconScore(unigram, goldFilename)
    testLexiconOutput(
        negCount, negBingo, negPredict, posCount, posBingo, posPredict)


if __name__ == '__main__':
    goldFilename = '../dataset/Semeval2013_test.csv'
    testNRCCanadaLexicon("NRC-Hashtag", goldFilename)
    testNRCCanadaLexicon("Sentiment140", goldFilename)
    testLiuBingLexicon(goldFilename)
    testMPQALexicon(goldFilename)
    testNRCEmotionLexicon(goldFilename)