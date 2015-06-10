__author__ = 'seven'
from replaceExpand import *


def lexiconScoreCaculator(tweet, dict, featureVector, ngramType):
    maxscore = 0
    lastscore = 0
    count = 0
    tmpNgram = []
    
    posscore = 0
    negscore = 0
    posmax = 0
    negmax = 0
    poscnt = 0
    negcnt = 0
    poslast = 0
    neglast = 0
    for i in range(len(tweet)):
        phrase = ""
        if ngramType == "unigram":
            phrase = tweet[i].strip(specialChar).lower()
        elif ngramType == "bigram" and i < (len(tweet)-1):
            phrase = tweet[i] + ' ' + tweet[i + 1]
            phrase = phrase.strip(specialChar).lower()
        tmpNgram.append(phrase)
        
        if phrase in dict:
            # print phrase
            score = dict[phrase]
            if score > 0:
                posscore += score
                poscnt += 1
                count += 1
                if score > posmax:
                    posmax = score
                if score > maxscore:
                    maxscore = score
                poslast = score
            elif score < 0:
                negscore += score
                negcnt += 1
                count += 1
                if abs(score) > negmax:
                    negmax = abs(score)
                if abs(score) > maxscore:
                    maxscore = abs(score)
                neglast = score

            lastscore = score
    posvec = [posscore, poscnt, poslast, posmax]
    negvec = [negscore, negcnt, neglast, -negmax]
    vec = [posscore + negscore, count, lastscore, maxscore]
    featureVector = featureVector + posvec + negvec + vec
    return tmpNgram, featureVector



def pariScoreCaculator(tmpNgram1, tmpNgram2, pairgram,
                count, lastscore, maxscore,
                negcnt, neglast, negmax, negscore,
                poscnt, poslast, posmax, posscore):
    for i in range(len(tmpNgram1)):
        for j in range(len(tmpNgram2)):
            phrase = tmpNgram1[i] + '---' + tmpNgram2[j]
            if phrase in pairgram:
                score = pairgram[phrase]
                # print phrase
                if score > 0:
                    posscore += score
                    poscnt += 1
                    count += 1
                    if score > posmax:
                        posmax = score
                    if score > maxscore:
                        maxscore = score
                    poslast = score
                elif score < 0:
                    negscore += score
                    negcnt += 1
                    count += 1
                    if abs(score) > negmax:
                        negmax = abs(score)
                    if abs(score) > maxscore:
                        maxscore = abs(score)
                    neglast = score

                lastscore = score
    return count, lastscore, maxscore, \
           negcnt, neglast, negmax, negscore, \
           poscnt, poslast, posmax, posscore