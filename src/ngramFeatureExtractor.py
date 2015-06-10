__author__ = 'seven'
from replaceExpand import *


def ngramVectorCreator(word, ngramModel, ngramVector):
    if word in ngramModel:
        ind = ngramModel.index(word)
        ngramVector[ind] = 1
    return ngramVector


def findWordgramFeature(tweet, uniModel, biModel, triModel, _4Model):
    vector = []
    tweet = [i.strip(specialChar).lower() for i in tweet]
    tweet = [i for i in tweet if i]

    uniVector = [0] * len(uniModel)
    for i in tweet:
        word = i.strip(specialChar).lower()
        uniVector = ngramVectorCreator(word, uniModel, uniVector)
    vector = vector + uniVector

    biVector = [0] * len(biModel)
    for i in range(len(tweet) - 1):
        phrase = tweet[i] + ' ' + tweet[i + 1]
        biVector = ngramVectorCreator(phrase, biModel, biVector)
    vector = vector + biVector

    triVector = [0] * len(triModel)
    for i in range(len(tweet) - 2):
        phrase = tweet[i] + ' ' + tweet[i + 1] + ' ' + tweet[i + 2]
        triVector = ngramVectorCreator(phrase, triModel, triVector)

        phrase = tweet[i] + ' ' + '*' + ' ' + tweet[i + 2]
        triVector = ngramVectorCreator(phrase, triModel, triVector)
    vector = vector + triVector

    _4Vector = [0] * len(_4Model)
    for i in range(len(tweet) - 3):
        phrase = tweet[i] + ' ' + tweet[i + 1] + ' ' + \
            tweet[i + 2] + ' ' + tweet[i + 3]
        _4Vector = ngramVectorCreator(phrase, _4Model, _4Vector)

        phrase = tweet[i] + ' ' + '*' + ' ' + \
            tweet[i + 2] + ' ' + tweet[i + 3]
        _4Vector = ngramVectorCreator(phrase, _4Model, _4Vector)

        phrase = tweet[i] + ' ' + tweet[i + 1] + ' ' + \
            '*' + ' ' + tweet[i + 3]
        _4Vector = ngramVectorCreator(phrase, _4Model, _4Vector)

    vector = vector + _4Vector

    return vector


def findChargramFeature(tweet, _3CharModel, _4CharModel, _5CharModel):
    vector = []
    tweet = [i.strip(specialChar).lower() for i in tweet]
    tweet = [i for i in tweet if i]

    _3CharVector = [0] * len(_3CharModel)
    for word in tweet:
        for index in xrange(len(word) - 2):
            seq = word[index:index + 3]
            _3CharVector = ngramVectorCreator(seq, _3CharModel, _3CharVector)
    vector = vector + _3CharVector

    _4CharVector = [0] * len(_4CharModel)
    for word in tweet:
        for index in xrange(len(word) - 3):
            seq = word[index:index + 4]
            _4CharVector = ngramVectorCreator(seq, _4CharModel, _4CharVector)
    vector = vector + _4CharVector

    _5CharVector = [0] * len(_5CharModel)
    for word in tweet:
        for index in xrange(len(word) - 4):
            seq = word[index:index + 5]
            _5CharVector = ngramVectorCreator(seq, _5CharModel, _5CharVector)
    vector = vector + _5CharVector

    return vector