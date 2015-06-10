import re

positive = 0
negative = 1
neutral = 2
objective = 2
total = 3
#specialChar = '1234567890#@%^&()_=`{}:"|[]\;\',./\n\t\r '
specialChar = '#@%^&()_=`{}:"|[]\;\',./\n\t\r '
listSpecialTag = ['#', 'U', '@', ',', 'E', '~', '$', 'G']


def replaceHashtag(tokens, POStags):
    """
    takes as input a list which contains words in tokens and
    return list of words in tokens after replacement
    eg #*** - > #
    """
    count = 0
    for i in range(len(tokens)):
        if POStags[i] == '#' or tokens[i].startswith('#'):
            count += 1
            POStags[i] = '#'
            tokens[i] = tokens[i][0:].strip(specialChar)
    return tokens, POStags, count


def removeNonEnglishWords(tokens, POStags):
    """
    remove the non-english or better non-ascii characters
    takes as input a list of words in tokens and a list of corresponding POStagss,
    not using POStagss now but may use in future
    and return the modified list of POStags and words
    """

    newTweet = []
    newToken = []
    for i in range(len(tokens)):
        if tokens[i] != '':
            chk = \
                re.match(
                    r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$',
                    tokens[i]
                )
            if chk:
                newTweet.append(tokens[i])
                newToken.append(POStags[i])
    return newTweet, newToken


def removeStopWords(tokens, POStags, stopWordsDict):
    """
    remove the stop words ,
    takes as input a list of words in tokens,
    a list of corresponding POStagss and a stopWords Dictonary,
    and return the modified list of POStags and words
    """

    newTweet = []
    newToken = []
    for i in range(len(tokens)):
        if stopWordsDict[tokens[i].lower().strip(specialChar)] == 0:
            newTweet.append(tokens[i])
            newToken.append(POStags[i])
    return newTweet, newToken


def replaceEmoticons(emoticonsDict, tokens, POStags):
    """
    replaces the emoticons present in tokens with its polarity
    takes as input a emoticons dict
    which has emoticons as key and polarity as value
    and a list which contains words in tokens
    and return list of words in tokens after replacement
    """

    for i in range(len(tokens)):
        if tokens[i] in emoticonsDict:
            # tokens[i] = emoticonsDict[tokens[i]]
            POStags[i] = 'E'
    return tokens, POStags


def expandAcronym(acronymDict, tokens, POStags):
    """
    expand the Acronym present in tokens
    takes as input a acronym dict
    which has acronym as key and abbreviation as value,
    a list which contains words in tokens and a list of POStags
    and return list of words in tokens after expansion and POStagss
    """
    newTweet = []
    newToken = []
    count = 0
    for i in range(len(tokens)):
        # word = tokens[i].lower().strip(specialChar)
        word = tokens[i].lower()
        if word:
            if word in acronymDict:
                count += 1
                newTweet += acronymDict[word][0]
                newToken += acronymDict[word][1]

            else:
                newTweet += [tokens[i]]
                newToken += [POStags[i]]
    # return newTweet, newToken, count
    return tokens, POStags, count


def replaceRepetition(tokens):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after replacement and numner of repetion
    eg coooooooool -> coool
    """
    count = 0
    for i in range(len(tokens)):
        x = list(tokens[i])
        if len(x) > 3:
            flag = 0
            for j in range(3, len(x)):
                if x[j - 3].lower() == x[j - 2].lower() == \
                        x[j - 1].lower() == x[j].lower():
                    x[j - 3] = ''

                    if flag == 0:
                        count += 1
                        flag = 1
            tokens[i] = ''.join(x).strip(specialChar)

    return tokens, count


def replaceNegation(tokens):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after replacement of "not","no","n't","~"
    eg isn't -> negation
    eg not -> negation
    """
    count = 0
    for i in range(len(tokens)):
        word = tokens[i].lower().strip(specialChar)
        if (word == "no" or word == "not" or word.count("n't") > 0):
            # tokens[i] = 'negation'
            count += 1
    return tokens, count


def expandNegation(tokens, POStags):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after expanding of "n't" to "not"
    eg isn't -> is not
    """

    newTweet = []
    newToken = []
    for i in range(len(tokens)):
        word = tokens[i].lower().strip(specialChar)
        if (word[-3:] == "n't"):
            if word[-5:] == "can't":
                newTweet.append('can')
            else:
                newTweet.append(word[:-3])
            newTweet.append('not')
            newToken.append('V')
            newToken.append('R')
        else:
            newTweet.append(tokens[i])
            newToken.append(POStags[i])
    return newTweet, newToken


def removeTarget(tokens, POStags):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after replacement
    eg @**** -> @
    """
    newToken = []
    newTweet = []
    countTarget = 0
    for i in range(len(tokens)):
        if POStags[i] == '@' or tokens[i].startswith('@'):
            countTarget += 1
            continue
        else:
            newTweet.append(tokens[i])
            newToken.append(POStags[i])
    return newTweet, newToken, countTarget


def removeUrl(tokens, POStags):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after replacement
    eg www.*.* ->'URL'
    """
    newToken = []
    newTweet = []
    countURL = 0
    for i in range(len(tokens)):
        if POStags[i] != 'U':
            newTweet.append(tokens[i])
            newToken.append(POStags[i])
        else:
            countURL += 1
    return newTweet, newToken, countURL


def removeNumbers(tokens, POStags):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after removing numbers
    """
    newToken = []
    newTweet = []
    for i in range(len(tokens)):
        if POStags[i] != '$':
            newTweet.append(tokens[i])
            newToken.append(POStags[i])
    return newTweet, newToken


def removeProperCommonNoun(tokens, POStags):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after removing common nouns
    """
    count = {'^': 0, 'Z': 0}
    newToken = []
    newTweet = []
    for i in range(len(tokens)):
        # if POStags[i] != '^' and POStags[i] != 'Z' and POStags[i] != 'O':
        if POStags[i] != '^' and POStags[i] != 'Z':
            newTweet.append(tokens[i])
            newToken.append(POStags[i])
        else:
            count[POStags[i]] += 1
    return newTweet, newToken
    # return tokens, POStags, [count['^'], count['Z']]

def removePreposition(tokens, POStags):
    """
    takes as input a list which contains words in tokens
    and return list of words in tokens after removing numbers
    """
    newToken = []
    newTweet = []
    countPreposition = 0
    for i in range(len(tokens)):
        if POStags[i] != 'P':
            newTweet.append(tokens[i])
            newToken.append(POStags[i])
        else:
            countPreposition += 1
    return newTweet, newToken
    # return tokens, POStags, countPreposition


def preprocesingTweet1(tokens, POStags, emoticonsDict, acronymDict):
    """preprocess the tokens """
    tokens, POStags = replaceEmoticons(emoticonsDict, tokens, POStags)
    tokens, POStags = removeNonEnglishWords(tokens, POStags)
    # tokens, POStags = removeNumbers(tokens, POStags)

    tokens, POStags, countAcronym = expandAcronym(acronymDict, tokens, POStags)
    tokens, countRepetition = replaceRepetition(tokens)
    tokens, POStags, countHashtag = replaceHashtag(tokens, POStags)
    tokens, POStags, countURL = removeUrl(tokens, POStags)
    tokens, POStags, countTarget = removeTarget(tokens, POStags)
    tokens, POStags = expandNegation(tokens, POStags)
    tokens, POStags = removeProperCommonNoun(tokens, POStags)
    tokens, POStags = removePreposition(tokens, POStags)
    return tokens, POStags, countAcronym, countRepetition, countHashtag, countURL, countTarget


def preprocesingTweet2(tokens, POStags, stopWords):
    """preprocess the tokens """
    tokens, countNegation = replaceNegation(tokens)
    tokens, POStags = removeStopWords(tokens, POStags, stopWords)
    return tokens, POStags, countNegation
