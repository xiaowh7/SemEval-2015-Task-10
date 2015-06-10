__author__ = 'seven'
from scoreCalculator import *


def findUniScore(tweet, unigram, vector):
    tmpUni, vector = lexiconScoreCaculator(tweet, unigram, vector, "unigram")
    return vector, tmpUni


def findBiScore(tweet, bigram, vector):
    tmpBi, vector = lexiconScoreCaculator(tweet, bigram, vector, "bigram")
    return vector, tmpBi


def findPairScore(tmpUni, tmpBi, pairgram, vector):
    # pair score
    lastscore = 0
    maxscore = 0
    count = 0

    posscore = 0
    negscore = 0
    posmax = 0
    negmax = 0
    poscnt = 0
    negcnt = 0
    poslast = 0
    neglast = 0

    count, lastscore, maxscore, \
    negcnt, neglast, negmax, negscore, \
    poscnt, poslast, posmax, posscore = pariScoreCaculator(
        tmpUni, tmpUni, pairgram,
        count, lastscore, maxscore,
        negcnt, neglast, negmax, negscore,
        poscnt, poslast, posmax, posscore
    )

    count, lastscore, maxscore, \
    negcnt, neglast, negmax, negscore, \
    poscnt, poslast, posmax, posscore = pariScoreCaculator(
        tmpUni, tmpBi, pairgram,
        count, lastscore, maxscore,
        negcnt, neglast, negmax, negscore,
        poscnt, poslast, posmax, posscore
    )

    count, lastscore, maxscore, \
    negcnt, neglast, negmax, negscore, \
    poscnt, poslast, posmax, posscore = pariScoreCaculator(
        tmpBi, tmpUni, pairgram,
        count, lastscore, maxscore,
        negcnt, neglast, negmax, negscore,
        poscnt, poslast, posmax, posscore
    )

    count, lastscore, maxscore, \
    negcnt, neglast, negmax, negscore, \
    poscnt, poslast, posmax, posscore = pariScoreCaculator(
        tmpBi, tmpBi, pairgram,
        count, lastscore, maxscore,
        negcnt, neglast, negmax, negscore,
        poscnt, poslast, posmax, posscore
    )

    posvec = [posscore, poscnt, poslast, posmax]
    negvec = [negscore, negcnt, neglast, -negmax]
    vec = [posscore + negscore, count, lastscore, maxscore]
    # print posvec + negvec + vec
    vector = vector + posvec + negvec + vec
    return vector


def findAutomaticLexiconScore(tweet, unigram, bigram, pairgram):
    vector = []

    vector, tmpUni = findUniScore(tweet, unigram, vector)

    vector, tmpBi = findBiScore(tweet, bigram, vector)

    vector = findPairScore(tmpUni, tmpBi, pairgram, vector)

    # totalscore = posscore + negscore
    # vector = vector + [totalscore, count, maxscore]
    return vector


def findManualLexiconScore(tweet, dict):
    vector = []
    tmpNgram, vector = lexiconScoreCaculator(tweet, dict, vector, "unigram")
    return vector


def findAFINNScore(tweet, dict):
    vector = []

    posscore = 0
    negscore = 0
    posmax = 0
    negmax = 0
    poscnt = 0
    negcnt = 0
    poslast = 0
    neglast = 0

    maxscore = 0
    lastscore = 0

    for i in range(len(tweet)):
        phrase = tweet[i].strip(specialChar).lower()
        if phrase in dict:
            # print phrase
            score = dict[phrase]
            if score > 0:
                posscore += score
                poscnt += 1
                # unicount += 1
                if score > posmax:
                    posmax = score
                if score > maxscore:
                    maxscore = score
                poslast = score
            elif score < 0:
                negscore += score
                negcnt += 1
                # unicount += 1
                if abs(score) > negmax:
                    negmax = abs(score)
                if abs(score) > maxscore:
                    maxscore = abs(score)
                neglast = score

            lastscore = score

        if not i == len(tweet) - 1:
            phrase = tweet[i] + ' ' + tweet[i + 1]
            phrase = phrase.strip(specialChar).lower()
            if phrase in dict:
                # print phrase
                score = dict[phrase]
                if score > 0:
                    posscore += score
                    poscnt += 1
                    # unicount += 1
                    if score > posmax:
                        posmax = score
                    if score > maxscore:
                        maxscore = score
                    poslast = score
                elif score < 0:
                    negscore += score
                    negcnt += 1
                    # unicount += 1
                    if abs(score) > negmax:
                        negmax = abs(score)
                    if abs(score) > maxscore:
                        maxscore = abs(score)
                    neglast = score

                lastscore = score

    posvec = [posscore, poscnt, poslast, posmax]
    negvec = [negscore, negcnt, neglast, -negmax]
    vec = [posscore + negscore, poscnt + negcnt, lastscore, maxscore]
    vector = vector + posvec + negvec + vec
    return vector