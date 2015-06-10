from replaceExpand import *


def findCapitalised(tokens, POStags):
    count = 0
    countCap = 0
    for i in range(len(tokens)):
        if POStags[i] != '$':
            word = tokens[i].strip(specialChar)
            if word:
                count += 1
                if word.isupper():
                    countCap += 1
    return [countCap]


def findNegation(tokens):
    countNegation = 0
    for i in range(len(tokens)):
        if tokens[i] == 'negation':
            countNegation += 1
    return [countNegation]


def findTotalScore(score):
    totalScore = 0
    for i in score.values():
        totalScore += (i[positive] - i[negative])
    return [totalScore]


def findPositiveNegativeWords(tokens, POStags, score):
    countPos = 0
    countNeg = 0
    count = 0
    totalScore = 0
    if tokens:
        for i in range(len(tokens)):
            if POStags[i] not in listSpecialTag:
                word = frozenset([tokens[i].lower().strip(specialChar)])
                if word:
                    count += 1
                    for phrase in score.keys():
                        if word.issubset(phrase):
                            if score[phrase][positive] != 0.0:
                                countPos += 1
                            if score[phrase][negative] != 0.0:
                                countNeg += 1
                            totalScore += \
                                (score[phrase][positive] -
                                 score[phrase][negative])
    return [countPos, countNeg, totalScore]


def findIntensifiers(tokens, POStags, intensifiers):
    countIntensifier = 0
    for i in range(len(tokens)):
        if tokens[i] in intensifiers:
            POStags[i] = 'Intensifier'
            countIntensifier += 1
    return [countIntensifier]


def findEmoticons(tokens, POStags, emoDict):
    countEmoPos = 0
    countEmoNeg = 0
    isLastEmoPos = 0
    isLastEmoNeg = 0
    isLastTokenEmoPos = 0
    isLastTokenEmoNeg = 0
    isFirstTokenEmoPos = 0
    isFirstTokenEmoNeg = 0
    for i in range(len(tokens)):
        if POStags[i] == 'E':
            if tokens[i] in emoDict:

                emo = emoDict[tokens[i]]
                if emo == 'Extremely-Positive' or emo == 'Positive':
                    # countEmoExtremePos += 1
                    countEmoPos += 1
                    isLastEmoPos = 1
                    isLastEmoNeg = 0
                if emo == 'Extremely-Negative' or emo == 'Negative':
                    # countEmoExtremeENeg += 1
                    countEmoNeg += 1
                    isLastEmoPos = 0
                    isLastEmoNeg = 1

                if i == len(tokens) - 1:
                    # print "The last POStags is Emoticon %s" % emo
                    if emo == 'Extremely-Positive' or emo == 'Positive':
                        isLastTokenEmoPos = 1
                    if emo == 'Extremely-Negative' or emo == 'Negative':
                        isLastTokenEmoNeg = 1
                elif i == 0:
                    # print "The first POStags is Emoticon %s" % emo
                    if emo == 'Extremely-Positive' or emo == 'Positive':
                        isFirstTokenEmoPos = 1
                    if emo == 'Extremely-Negative' or emo == 'Negative':
                        isFirstTokenEmoNeg = 1
    return [countEmoPos, countEmoNeg,
            isLastEmoPos, isLastEmoNeg,
            isFirstTokenEmoPos, isFirstTokenEmoNeg,
            isLastTokenEmoPos, isLastTokenEmoNeg]


def findHashtag(tokens, POStags):
    count = 0
    hashtags = []
    for i in range(len(tokens)):
        if POStags[i] == '#':
            count += 1
            hashtag = tokens[i].strip(specialChar).lower()
            hashtags.append(hashtag)
    return hashtags


def countSpecialChar(tokens):
    count = {'?': 0, '!': 0}
    position = {'?': 0, '!': 0}
    max = {'?': 0, '!': 0}
    # contiguousSequence = {'??': 0, '!!': 0, '!?': 0, '?!': 0}
    isLastExclamation = 0
    isLastQuestion = 0
    # count={'?':[0,0],'!':[0,0],'*':[0,0]}
    for i in range(len(tokens)):
        word = tokens[i].lower().strip(specialChar)
        # word=frozenset([tokens[i].lower().strip(specialChar)])
        if word:
            for symbol in count:
                cnt = word.count(symbol)
                if cnt > 0:
                    count[symbol] += cnt
                    if count[symbol] == cnt:
                        position[symbol] = i
                    if cnt > max[symbol]:
                        max[symbol] = cnt

            if i == len(tokens) - 1:
                if word.count('?') > 0:
                    isLastQuestion = 1
                if word.count('!') > 0:
                    isLastExclamation = 1

    return [count['?'], count['!'],
            position['?'], position['!'],
            isLastExclamation, isLastQuestion]


def countPOStag(tokens, POStags):
    count = {'N': 0, 'V': 0, 'R': 0, 'P': 0, 'O': 0, 'A': 0}
    words = {'N': [], 'V': [], 'R': [], 'P': [], 'O': [], 'A': []}
    for i in range(len(tokens)):
        word = tokens[i].lower().strip(specialChar)
        # word=frozenset([tokens[i].lower().strip(specialChar)])
        if word:
            if POStags[i] in count:
                count[POStags[i]] += 1
                words[POStags[i]].append(word)
    return [count['N'], count['V'], count['R'],
            count['P'], count['O'], count['A']], \
           words


def findUrl(tokens, POStags):
    count = 0
    for i in range(len(tokens)):
        if POStags[i] == 'U':
            count += 1
    return [count]


def findFeatures(tokens, POStags,
                 stopWords, emoticonsDict, acronymDict, intensifiers):
    """takes as input the tokens and POStags and returns the feature vector"""

    tokens, POStags, \
    countAcronym, countRepetition, countHashtag, countURL, countTarget \
        = preprocesingTweet1(tokens, POStags, emoticonsDict, acronymDict)
    featureVector = []

    # number of each POS tag
    countPOStagVector, words = countPOStag(tokens, POStags)
    featureVector.extend(countPOStagVector)

    tokens, POStags, countNegation = preprocesingTweet2(tokens, POStags, stopWords)
    featureVector.extend(findCapitalised(tokens, POStags))
    featureVector.extend(findEmoticons(tokens, POStags, emoticonsDict))
    # featureVector.extend(findIntensifiers(tokens, POStags, intensifiers))
    # featureVector.extend(findUrl(tokens,POStags))

    # number of acronym
    featureVector.extend([countAcronym])
    # number of words which had repetion
    featureVector.extend([countRepetition])
    # number of negtation
    featureVector.extend([countNegation])
    # number of hashtag
    featureVector.extend([countHashtag])
    # number of preposition
    # featureVector.extend([countPreposition])
    # number of URL
    # featureVector.extend([countURL])
    # number of @
    # featureVector.extend([countTarget])
    # number of special char
    featureVector.extend(countSpecialChar(tokens))

    hashtags = findHashtag(tokens, POStags)

    return featureVector, words, hashtags, tokens