from replaceExpand import *
from collections import defaultdict


def init(dataset):
    if dataset == "Semeval2014" or dataset == "SemEval2014" or \
                    dataset == "semeval2014":
        trainFilename = "../dataset/trainset/train.csv"
        testFilename = "../dataset/SemEval2014-Task9/" \
                       "SemEval2014_test.csv"
        trainDepFilename = "../dataset/trainset/train_dependency.txt"
        testDepFilename = "../dataset/SemEval2014-Task9/" \
                          "SemEval2014_test_dependency.txt"
        goldFilename = "../dataset/SemEval2014-Task9/" \
                           "SemEval2015-task10-test-B-input-progress.txt"
    elif dataset == "Semeval2015" or dataset == "SemEval2015" or \
                    dataset == "semeval2015":
        trainFilename = "../dataset/trainset/train.csv"
        testFilename = "../dataset/SemEval2015-Task10/" \
                       "SemEval2015_test.csv"
        trainDepFilename = "../dataset/trainset/train_dependency.txt"
        testDepFilename = "../dataset/SemEval2015-Task10/" \
                          "SemEval2015_test_dependency.txt"
        goldFilename = "../dataset/SemEval2015-Task10/" \
                       "SemEval2015-task10-test-B-input.txt"
    elif dataset == "Semeval2013" or dataset == "SemEval2013" or \
                    dataset == "semeval2013":
        trainFilename = "../dataset/trainset/train.csv"
        testFilename = "../dataset/SemEval2013-Task2B/tweet/" \
                       "Semeval2013_test.csv"
        trainDepFilename = "../dataset/trainset/train_dependency.txt"
        testDepFilename = "../dataset/SemEval2013-Task2B/tweet/" \
                          "Semeval2013_test_dependency.txt"
        goldFilename = "../dataset/SemEval2013-Task2B/tweet/" \
                       "Semeval2013_gold.csv"
    elif dataset == "Twitter-2013" or dataset == "Twitter-2014":
        trainFilename = "../dataset/trainset/train.csv"
        testFilename = \
            "../dataset/SemEval2014-Task9/%s/%s_test.csv" % (dataset, dataset)
        trainDepFilename = "../dataset/trainset/train_dependency.txt"
        testDepFilename = "../dataset/SemEval2014-Task9/%s/%s_dependency.txt" \
                          % (dataset, dataset)
        goldFilename = \
            "../dataset/SemEval2014-Task9/%s/%s_gold.csv" % (dataset, dataset)
    elif dataset == "Real-time":
        trainFilename = "../dataset/%s/%s_train.csv" % (dataset, dataset)
        testFilename = "../dataset/%s/%s_test.csv" % (dataset, dataset)
        trainDepFilename = "../dataset/%s/%s_train_dependency.txt" \
                           % (dataset, dataset)
        testDepFilename = "../dataset/%s/%s_test_dependency.txt" \
                          % (dataset, dataset)
        goldFilename = "../dataset/%s/%s_gold.csv" % (dataset, dataset)
    else:
        exit("Error: Wrong dataset\nPlease specify a valid dataset.")

    return trainFilename, testFilename, \
           trainDepFilename, testDepFilename, goldFilename


def initAdditionalTrainset(addTrainsetName):
    if addTrainsetName == "SentiStrength" or addTrainsetName == "sanders":
        addTrainsetFilename = \
            "../dataset/additionalTrainset/%s/%s_train.csv" % \
            (addTrainsetName, addTrainsetName)
        addTrainsetDepFilename = \
            "../dataset/additionalTrainset/%s/%s_dependency.txt" % \
            (addTrainsetName, addTrainsetName)
    else:
        exit("Error: Wrong additional trainset\n"
             "Please specify a valid additional trainset.")

    return addTrainsetFilename, addTrainsetDepFilename


def loadDictionary():
    """
    Load dictionaries
    :return: acronymDict, emoticonsDict
    """
    # create acronym dictionary
    print "Loading acronym dictionary..."
    AcronymFilename = "..//requirement//dictionary//acronym.txt"
    infile = open(AcronymFilename, 'r')
    data = infile.read().split('\n')
    acronymDict = {}
    for i in data:
        if i:
            i = i.split('\t')
            word = i[0].split()
            token = i[1].split()[1:]
            key = word[0].lower().strip(specialChar)
            value = [j.lower().strip(specialChar) for j in word[1:]]
            acronymDict[key] = [value, token]
    infile.close()
    # print acronymDict

    # create emoticons dictionary
    print "Loading emoticons dictionary..."
    EmoticonsFilename = \
        "..//requirement//dictionary//emoticonsWithPolarity.txt"
    f = open(EmoticonsFilename, 'r')
    data = f.read().split('\n')
    emoticonsDict = {}
    for i in data:
        if i:
            i = i.split()
            value = i[-1]
            key = i[:-1]
            for j in key:
                emoticonsDict[j] = value
    f.close()
    # print emoticonsDict

    return acronymDict, emoticonsDict


def loadOtherReferences():
    """
    Load other references
    :return: stopWords, intensifiers
    """
    print "Loading stopwords..."
    StopwordsFilename = "..//requirement//other//stopWords.txt"
    stopWords = defaultdict(int)
    infile = open(StopwordsFilename, "r")
    for line in infile:
        if line:
            line = line.strip(specialChar).lower()
            stopWords[line] = 1
    infile.close()

    print "Loading intersifiers..."
    IntensifierFilename = "..//requirement//other//intensifier.txt"
    intensifiers = []
    infile = open(IntensifierFilename, 'r')
    for word in infile.readlines():
        word = word.strip('\n\t')
        intensifiers.append(word)
    infile.close()

    return stopWords, intensifiers


def ngramReader(ngramModel, ngramFilename):
    ngramfile = open(ngramFilename, 'r')
    for line in ngramfile:
        if line:
            line = line.strip('\r\t\n ')
            ngramModel.append(line)
    uniModel = list(set(ngramModel))
    uniModel.sort()
    ngramfile.close()
    return uniModel


def loadNgram(dataset):
    if dataset == "Semeval2014" or dataset == "SemEval2014" or \
                    dataset == "Semeval2015" or dataset == "SemEval2015" or \
                    dataset == "semeval2014" or dataset == "semeval2015" or \
                    dataset == "Twitter-2013" or dataset == "Twitter-2014":
        unigramfile = "..//requirement//ngram//Semeval//Semeval_unigram.txt"
        bigramfile = "..//requirement//ngram//Semeval//Semeval_bigram.txt"
        trigramfile = "..//requirement//ngram//Semeval//Semeval_trigram.txt"
        _4gramfile = "..//requirement//ngram//Semeval//Semeval_4gram.txt"
        _3Chargramfile = \
            "..//requirement//ngram//Semeval//Semeval_3Chargram.txt"
        _4Chargramfile = \
            "..//requirement//ngram//Semeval//Semeval_4Chargram.txt"
        _5Chargramfile = \
            "..//requirement//ngram//Semeval//Semeval_5Chargram.txt"
        # unigramfile = "..//requirement//ngram//" \
        #               "Semeval-dev//Semeval-dev_unigram.txt"
        # bigramfile = "..//requirement//ngram//" \
        #              "Semeval-dev//Semeval-dev_bigram.txt"
        # trigramfile = "..//requirement//ngram//" \
        #               "Semeval-dev//Semeval-dev_trigram.txt"
        # _4gramfile = "..//requirement//ngram//" \
        #              "Semeval-dev//Semeval-dev_4gram.txt"
        # _3Chargramfile = \
        #     "..//requirement//ngram//Semeval-dev//Semeval-dev_3Chargram.txt"
        # _4Chargramfile = \
        #     "..//requirement//ngram//Semeval-dev//Semeval-dev_4Chargram.txt"
        # _5Chargramfile = \
        #     "..//requirement//ngram//Semeval-dev//Semeval-dev_5Chargram.txt"
    elif dataset == "Real-time":
        unigramfile = \
            "..//requirement//ngram//%s//%s_unigram.txt" % (dataset, dataset)
        bigramfile = \
            "..//requirement//ngram//%s//%s_bigram.txt" % (dataset, dataset)
        trigramfile = \
            "..//requirement//ngram//%s//%s_trigram.txt" % (dataset, dataset)
        _4gramfile = \
            "..//requirement//ngram//%s//%s_4gram.txt" % (dataset, dataset)
        _3Chargramfile = \
            "..//requirement//ngram//%s//%s_3Chargram.txt" % (dataset, dataset)
        _4Chargramfile = \
            "..//requirement//ngram//%s//%s_4Chargram.txt" % (dataset, dataset)
        _5Chargramfile = \
            "..//requirement//ngram//%s//%s_5Chargram.txt" % (dataset, dataset)
    else:
        exit("Error: Wrong dataset\nPlease specify a valid dataset.")

    print "Creating Unigram Model......."
    uniModel = []
    uniModel = ngramReader(uniModel, unigramfile)
    print "Unigram Model Created, total %s" % len(uniModel)

    print "Creating Bigram Model......."
    biModel = []
    biModel = ngramReader(biModel, bigramfile)
    print "Bigram Model Created, total %s" % len(biModel)

    print "Creating Trigram Model......."
    triModel = []
    triModel = ngramReader(triModel, trigramfile)
    print "Trigram Model Created, total %s" % len(triModel)

    print "Creating 4gram Model......."
    _4Model = []
    _4Model = ngramReader(_4Model, _4gramfile)
    print "F4gram Model Created, total %s" % len(_4Model)

    print "Creating 3 Characters gram Model......."
    _3CharModel = []
    _3CharModel = ngramReader(_3CharModel, _3Chargramfile)
    print "3 Characters gram Model Created, total %s" % len(_3CharModel)

    print "Creating 4 Characters gram Model......."
    _4CharModel = []
    _4CharModel = ngramReader(_4CharModel, _4Chargramfile)
    print "4 Characters gram Model Created, total %s" % len(_4CharModel)

    print "Creating 5 Characters gram Model......."
    _5CharModel = []
    _5CharModel = ngramReader(_5CharModel, _5Chargramfile)
    print "5 Characters gram Model Created, total %s" % len(_5CharModel)

    return uniModel, biModel, triModel, _4Model, \
           _3CharModel, _4CharModel, _5CharModel


def NRCCanadaLexiconReader(ngram, ngramFilename):
    inFile = open(ngramFilename, 'r')
    for line in inFile.readlines():
        raw = line.split('\t')
        phrase = raw[0]
        score = float(raw[1])
        ngram[phrase] = score
    inFile.close()
    return ngram


def loadNRCCanadaLexicon(src):
    print "Loading NRC-Canada %s lexicon..." % src

    if src == "NRC-Hashtag":
        source = "NRC-Hashtag-Sentiment-Lexicon-v0.1"
    elif src == "Sentiment140":
        source = "Sentiment140-Lexicon-v0.1"
    else:
        exit("Error: Wrong NRCLexicon source\n"
             "Please specify a valid source(NRC-Hashtag or Sentiment140).")
    unigramFilename = \
        "..//requirement//lexicon//" \
        "NRC-Canada//%s//%s//unigrams-pmilexicon.txt" \
        % (source, source)
    unigram = {}
    unigram = NRCCanadaLexiconReader(unigram, unigramFilename)

    bigramFilename = \
        "..//requirement//lexicon//" \
        "NRC-Canada//%s//%s//bigrams-pmilexicon.txt" \
        % (source, source)
    bigram = {}
    bigram = NRCCanadaLexiconReader(bigram, bigramFilename)

    pairsFilename = \
        "..//requirement//lexicon//" \
        "NRC-Canada//%s//%s//pairs-pmilexicon.txt" \
        % (source, source)
    pairs = {}
    pairs = NRCCanadaLexiconReader(pairs, pairsFilename)

    return unigram, bigram, pairs


def loadSentiment140Lexicon(src):
    if src == "Sentiment140":
        source = "Sentiment140-Lexicon-v0.1"
    else:
        exit("Error: Wrong NRCLexicon source\n"
             "Please specify a valid source(NRC-Hashtag or Sentiment140).")
    unigramFilename = \
        "..//requirement//lexicon//" \
        "NRC-Canada//%s//%s//uniLexicon.txt" \
        % (source, source)
    unigram = {}
    unigram = NRCCanadaLexiconReader(unigram, unigramFilename)

    bigramFilename = \
        "..//requirement//lexicon//" \
        "NRC-Canada//%s//%s//biLexicon.txt" \
        % (source, source)
    bigram = {}
    bigram = NRCCanadaLexiconReader(bigram, bigramFilename)

    pairsFilename = \
        "..//requirement//lexicon//" \
        "NRC-Canada//%s//%s//pairs-pmilexicon.txt" \
        % (source, source)
    pairs = {}
    pairs = NRCCanadaLexiconReader(pairs, pairsFilename)

    return unigram, bigram, pairs

def loadLiuBingLexicon():
    print "Loading LiuBing lexicon..."
    dict = {}
    LiuBingLexiconPosFilename = \
        '..//requirement//lexicon//LiuBingLexicon//positive-words.txt'
    inFile = open(LiuBingLexiconPosFilename, 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = 1
    inFile.close()

    LiuBingLexiconNegFilename = \
        '..//requirement//lexicon//LiuBingLexicon//negative-words.txt'
    inFile = open(LiuBingLexiconNegFilename, 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = -1
    inFile.close()
    return dict


def loadMPQALexicon():
    print "Loading MPQA lexicon..."
    dict = {}
    MPQALexiconFilename = \
        '..//requirement//lexicon//MPQALexicon//MPQALexicon//' \
        'subjclueslen1-HLTEMNLP05.tff'
    inFile = open(MPQALexiconFilename, 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t').split(' ')
        type = line[0][5:]
        word = line[2][6:]
        polarity = line[5][14:]
        score = 1
        if type == 'strongsubj':
            score = 2
        if polarity == 'negative':
            score *= -1
        dict[word] = score
    inFile.close()
    return dict


def loadNRCEmoticonLexicon():
    print "Loading NRCEmoticon lexicon..."
    dict = {}
    NRCEmoticonFilename = \
        '..//requirement//lexicon//NRC-Canada//NRC-Emotion-Lexicon-v0.92//' \
        'NRC-Emotion-Lexicon-v0.92//' \
        'NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'
    inFile = open(NRCEmoticonFilename, 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t').split('\t')
        word = line[0]
        category = line[1]
        assoFlag = line[2]
        score = 1
        if assoFlag == '1':
            if category == 'anger' or category == 'fear' or \
                            category == 'sadness' or category == 'disgust' or \
                            category == 'negative':
                score = -1
            dict[word] = score
    inFile.close()
    return dict


def loadPosNegWords():
    print "Loading PosNegWords lexicon..."
    dict = {}
    PosWordsFilename = '..//requirement//lexicon//PosNegWords//pos_mod.txt'
    inFile = open(PosWordsFilename, 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = 1
    inFile.close()

    NegWordsFilename = '..//requirement//lexicon//PosNegWords//neg_mod.txt'
    inFile = open(NegWordsFilename, 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = -1
    inFile.close()
    return dict


def loadAFINNLexicon():
    print "Loading AFINN lexicon..."
    dict = {}
    AFINNLexiconFilename = '..//requirement//lexicon//AFINN//AFINN-111.txt'
    inFile = open(AFINNLexiconFilename, 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t').split('\t')
        dict[line[0]] = int(line[1])
    inFile.close()
    return dict


def getDependency(filename):
    """
    read dependencies from file
    :param filename:
    :return:
        dependencies in form {key: type, value: [word1, word2]}
    """
    infile = open(filename, 'r')
    dependencies = []
    pattern = re.compile("[(),-]")
    for line in infile.readlines():
        dpds = line.strip('\t\n').split('\t')
        ans = {}
        for dpd in dpds:
            match = re.split(pattern, dpd)
            # print match
            word1, word2, type = match[1], match[3], match[0]
            # phrase = "%s %s" %(word1, word2)
            # print word1, word2, dependency
            if type not in ans:
                ans[type] = [[word1, word2]]
            else:
                ans[type].append([word1, word2])
        dependencies.append(ans)

    return dependencies


# def loadDependency(trainDepFilename, testDepFilename):
#     print "Loading trainset dependencies..."
#     trainDependicies = getDependency(trainDepFilename)
#     print "Loading testset dependencies..."
#     testDependicies = getDependency(testDepFilename)
#     return trainDependicies, testDependicies