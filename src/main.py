__author__ = 'seven'
from ngramFeatureExtractor import *
from lexiconFeatureExtractor import *
from syntaxFeatureExtractor import *
from contextFeatureExtractor import *
from classifier import *
from prepare import *
from output import *
from svmutil import *


def checkArguments():
    modelFilename = sys.argv[1]
    dataset = sys.argv[2]
    addTrainsetList = []
    if len(sys.argv) >= 4:
        for index in xrange(3, len(sys.argv)):
            addTrainsetList.append(sys.argv[index])

    return dataset, addTrainsetList, modelFilename


def getScoreFeatureVector(words, vector):
    # find lexicon score for each word
    vec = []
    Sentiment140Vector, tmplist = findUniScore(words, S140Unigram, vec)
    vector = vector + Sentiment140Vector

    vec = []
    NRCHashtagVector, tmplist = findUniScore(words, NRCUnigram, vec)
    vector = vector + NRCHashtagVector

    LiuBingVector = findManualLexiconScore(words, LiuBingDict)
    vector = vector + LiuBingVector

    MPQAVector = findManualLexiconScore(words, MPQADict)
    vector = vector + MPQAVector

    NRCEmoticonVector = findManualLexiconScore(words, NRCEmotionDict)
    vector = vector + NRCEmoticonVector

    PosNegWordsDictVector = findManualLexiconScore(words, PosNegWordsDict)
    vector = vector + PosNegWordsDictVector

    AFINNVector = findAFINNScore(words, AFINNDict)
    vector = vector + AFINNVector
    # print vector
    return vector


def createFeatureVectors(datafile, dependencies):
    labels = []
    featureVectors = []
    index = 0
    infile = open(datafile, 'r')
    for line in infile:
        if line:
            content = line.split('\t')
            tokens = content[1].split()
            POStags = content[2].split()
            label = content[3].strip()
            dependency = dependencies[index]
            index += 1

            if tokens:
                labels.append(encode[label])
                vector, words, hashtags, tokens = \
                    findFeatures(tokens, POStags, stopwords, emoticonsDict,
                                 acronymDict, intensifiers)

                # find char and word gram feature
                chargramVector = findChargramFeature(
                    tokens, _3ChargramModel, _4ChargramModel, _5ChargramModel)
                vector.extend(chargramVector)

                wordgramVector = \
                    findWordgramFeature(tokens, unigramModel, bigramModel,
                                        trigramModel, _4gramModel)
                vector.extend(wordgramVector)

                # find context feature
                S140ContextVector = \
                    findContextFeature(dependency, S140Unigram, emoticonsDict)
                vector.extend(S140ContextVector)

                NRCContextVector = \
                    findContextFeature(dependency, NRCUnigram, emoticonsDict)
                vector.extend(NRCContextVector)

                MPQAContextVector = \
                    findContextFeature1(dependency, MPQADict, intensifiers)
                vector.extend(MPQAContextVector)

                # find lexicon for each capitalised word
                # vector = getScoreFeatureVector(capWords, vector)

                # find hashtag score for each hashtag
                vector = getScoreFeatureVector(hashtags, vector)

                # find lexicon score for each pos-tags
                tags = ['N', 'V', 'R', 'O', 'A']
                for pos in words:
                    if pos in tags:
                        vector = getScoreFeatureVector(words[pos], vector)

                # find score for each lexicon
                S140Vector = \
                    findAutomaticLexiconScore(
                        tokens, S140Unigram, S140Bigram, S140Pairs)
                vector.extend(S140Vector)

                NRCVector = \
                    findAutomaticLexiconScore(
                        tokens, NRCUnigram, NRCBigram, NRCPairs)
                vector.extend(NRCVector)

                LiuBingVector = findManualLexiconScore(tokens, LiuBingDict)
                vector.extend(LiuBingVector)

                MPQAVector = findManualLexiconScore(tokens, MPQADict)
                vector.extend(MPQAVector)

                NRCEmotionVector = \
                    findManualLexiconScore(tokens, NRCEmotionDict)
                vector.extend(NRCEmotionVector)

                PosNegWordsDictVector = \
                    findManualLexiconScore(tokens, PosNegWordsDict)
                vector.extend(PosNegWordsDictVector)

                AFINNVector = findAFINNScore(tokens, AFINNDict)
                vector.extend(AFINNVector)

                featureVectors.append(vector)
    infile.close()
    return labels, featureVectors


def combineAdditionalTrainset(addTrainsetList, trainLabel, trainFeatureVectors):
    for addTrainset in addTrainsetList:
        addTrainsetFilename, addTrainsetDepFilename = \
            initAdditionalTrainset(addTrainset)
        addTrainDependencies = getDependency(addTrainsetDepFilename)
        addTrainLabel, addTrainFeatureVectors = \
            createFeatureVectors(addTrainsetFilename, addTrainDependencies)
        for index in xrange(len(addTrainLabel)):
            trainLabel.append(addTrainLabel[index])
            trainFeatureVectors.append(addTrainFeatureVectors[index])
        # print len(trainLabel)

    return trainLabel, trainFeatureVectors


def trainNewModel():
    """Create feature vectors of training set """
    print "Creating feature vectors for trainset..."
    trainDependencies = getDependency(trainDepFilename)
    trainLabel, trainFeatureVectors = \
        createFeatureVectors(trainFilename, trainDependencies)
    print "Length of feature vector for trainset: %d" \
          % len(trainFeatureVectors[0])
    if not len(addTrainsetList) == 0:
        print "Combining feature vectors of additional trainset..."
        trainLabel, trainFeatureVectors = \
            combineAdditionalTrainset(
                addTrainsetList, trainLabel, trainFeatureVectors)
    print "Feature vectors of trainset created."
    SVMTrain(trainLabel, trainFeatureVectors, modelFilename)


if __name__ == '__main__':

    """check arguments"""
    if len(sys.argv) < 2:
        print "Usage :: python main.py model dataset " \
              "additionalTrainset additionalTrainset ..."
        sys.exit("Error: wrong arguments")
    else:
        dataset, addTrainsetList, modelFilename = checkArguments()
        encode = {'positive': 1.0, 'negative': 2.0, 'neutral': 3.0,
                  'unknwn': 3.0}
        decode = {1.0: 'positive', 2.0: 'negative', 3.0: 'neutral'}
        trainFilename, testFilename, \
            trainDepFilename, testDepFilename, goldFilename = \
            init(dataset)
        goldStandard = []
        predictLabel = []
        unigramModel, bigramModel, trigramModel, _4gramModel, \
        _3ChargramModel, _4ChargramModel, _5ChargramModel = \
        loadNgram(dataset)

    acronymDict, emoticonsDict = loadDictionary()
    stopwords, intensifiers = loadOtherReferences()

    S140Unigram, S140Bigram, S140Pairs = loadNRCCanadaLexicon("Sentiment140")
    NRCUnigram, NRCBigram, NRCPairs = loadNRCCanadaLexicon("NRC-Hashtag")

    LiuBingDict = loadLiuBingLexicon()
    MPQADict = loadMPQALexicon()
    NRCEmotionDict = loadNRCEmoticonLexicon()
    PosNegWordsDict = loadPosNegWords()
    AFINNDict = loadAFINNLexicon()

    isTrainRequired = raw_input("Train new model? (y for yes):")
    if isTrainRequired == "yes" or isTrainRequired == "y":
        trainNewModel()

    """Create feature vectors of testset """
    print "Creating feature vectors for testset..."
    testDependencies = getDependency(testDepFilename)
    testLabel, testFeatureVectors = \
        createFeatureVectors(testFilename, testDependencies)

    print "Length of feature vector for testset: %d" \
          % len(testFeatureVectors[0])
    print "Feature vectors of testset created."

    for i in range(len(testLabel)):
        goldStandard.append(decode[testLabel[i]])

    encodePredictLabel = SVMTest(testLabel, testFeatureVectors, modelFilename)

    for i in range(len(encodePredictLabel)):
        predictLabel.append(decode[encodePredictLabel[i]])

    output(dataset, addTrainsetList, goldFilename, predictLabel)