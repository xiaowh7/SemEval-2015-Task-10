__author__ = 'seven'
def findContextFeature(dependencies, unigram, emoticonsDict):
    vector = []

    #for dependency type amod, advmod, tmod, vmod
    modifyPosscore = 0
    modifyNegscore = 0
    modifyCount = 0
    modifyMax = 0
    modifyLastscore = 0

    modifiedPosscore = 0
    modifiedNegscore = 0
    modifiedCount = 0
    modifiedMax = 0
    modifiedLastscore = 0

    #for dependency type conj, cc
    conjPosscore = 0
    conjNegscore = 0
    conjCount = 0
    conjMax = 0
    conjLastscore = 0

    copPosscore = 0
    copNegscore = 0
    copCount = 0
    copMax = 0
    copLastscore = 0

    for type in dependencies:
        if type == "amod" or type == "advmod":
            for dpd in dependencies[type]:
                ###########################################################
                #modify feature for type mod
                word1 = dpd[0].lower()
                #GET the score
                score = 0
                if word1 in unigram and not (word1.startswith("@") or word1.startswith("http://")):
                    score = unigram[word1]

                if score > 0:
                    modifyPosscore += score
                    modifyCount += 1
                    if score > modifyMax:
                        modifyMax = score
                elif score < 0:
                    modifyNegscore += score
                    modifyCount += 1
                    if abs(score) > modifyMax:
                        modifyMax = score

                    modifyLastscore = score
                    ############################################################

                    ###########################################################
                    #modified feature for type mod
                word2 = dpd[1].lower()
                #GET the score
                score = 0
                if word2 in unigram and not (word2.startswith("@") or word2.startswith("http://")):
                    score = unigram[word2]
                elif word2 in emoticonsDict:
                    emo = emoticonsDict[word2]
                    if emo == 'Extremely-Positive' or emo == 'Positive':
                        score = 5
                    if emo == 'Extremely-Negative' or emo == 'Negative':
                        score = -5

                if score > 0:
                    modifiedPosscore += score
                    modifiedCount += 1
                    if score > modifiedMax:
                        modifiedMax = score
                elif score < 0:
                    modifiedNegscore += score
                    modifiedCount += 1
                    if abs(score) > modifiedMax:
                        modifiedMax = score

                modifiedLastscore = score
                ############################################################

        if type == "conj" or type == "cc":
            for dpd in dependencies[type]:
                word1 = dpd[0].lower()
                word2 = dpd[1].lower()
                #get the score
                score = 0
                if word2 in unigram and not (word2.startswith("@") or word2.startswith("https://")):
                    score += unigram[word2]
                if word1 in unigram and not (word1.startswith("@") or word1.startswith("https://")):
                    score += unigram[word1]

                if score > 0:
                    conjPosscore += score
                    conjCount += 1
                    if score > conjMax:
                        conjMax = score
                elif score < 0:
                    conjNegscore += score
                    conjCount += 1
                    if abs(score) > conjMax:
                        conjMax = score

                conjLastscore = score

        # if type == "cop":
        #     for dpd in dependencies[type]:
        #         word2 = dpd[1].lower()
        #         # word2 = dpd[1].lower()
        #         #get the score
        #         score = 0
        #
        #         if word2 in unigram and not (word2.startswith("https://")):
        #             score += unigram[word2]
        #
        #         if score > 0:
        #             copPosscore += score
        #             copCount += 1
        #             if score > copMax:
        #                 copMax = score
        #         elif score < 0:
        #             copNegscore += score
        #             copCount += 1
        #             if abs(score) > copMax:
        #                 copMax = score
        #
        #         copLastscore = score

    # modifyVec = [modifyPosscore, modifyNegscore, modifyCount, modifyMax, modifyLastscore]
    # modifiedVec = [modifiedPosscore, modifiedNegscore, modifiedCount, modifiedMax, modifiedLastscore]
    modifyVec = [modifyPosscore, modifyNegscore, modifyMax, modifyLastscore]
    modifiedVec = [modifiedPosscore, modifiedNegscore, modifiedMax, modifiedLastscore]
    conjVec = [conjPosscore, conjNegscore, conjMax, conjLastscore]
    # copVec = [copPosscore, copNegscore, copMax, copLastscore]
    # subjVec = [subjPosscore, subjNegscore, subjCount, subjMax, subjLastscore]
    # objVec = [objPosscore, objNegscore, objCount, objMax, objLastscore]
    # vector = vector + modifyVec + modifiedVec + subjVec + objVec
    vector = vector + modifyVec + modifiedVec + conjVec
    # print vector
    return vector


def findContextFeature1(dependencies, dict, intensifiers):
    #for dependency type neg
    isNegExist = 0

    rcmodScore = 0
    isRcmodExist = 0

    copScore = 0
    iscopExist = 0

    depScore = 0
    isDepExist = 0

    vector = []
    preByAdj = 0
    preByAdv = 0
    preByIntensifier = 0
    modifyStrSubj = 0
    modifyWeakSubj = 0
    modifiedStrSubj = 0
    modifiedWeakSubj = 0
    for type in dependencies:
        #get the feature preByAdj
        if type == "amod" or type == "acomp":
            preByAdj = 1

        #get the feature preByAdv
        if type == "advmod" or type == "advcl" or type == "npadvmod":
            preByAdv = 1

        #get the feature isNegExist
        if type == "neg":
            isNegExist = 1

        if type == "remod" or type == "acomp":
            isRcmodExist = 1
            for dpd in dependencies[type]:
                # word1 = dpd[0]
                word2 = dpd[1].lower()
                #get the score
                score = 0
                if word2 in dict:
                    score = dict[word2]
                if word2[-2:] == "ed":
                    word2_tmp = word2[:-1]
                    if word2_tmp in dict:
                        score += dict[word2]

                rcmodScore += score

        if type == "cop":
            iscopExist = 1

        if type == "dep":
            isdepExist = 1
            for dpd in dependencies[type]:
                word1 = dpd[0].lower()
                score = 0
                if word1 in dict:
                    score = dict[word1]

                depScore += score

        #get the feature preByIntensifier
        if type == "advmod":
            for dpd in dependencies[type]:
                word2 = dpd[1].lower()
                if word2 in intensifiers:
                    preByIntensifier = 1

        #get the feature modifyStrSubj, modifyWeakSubj, modifiedStrSubj,modifiedWeakSubj
        if type == "advmod" or type == "amod" or type == "partmod":
            for dpd in dependencies[type]:
                word1 = dpd[0].lower()
                word2 = dpd[1].lower()
                if word1 in dict:
                    score = dict[word1]
                    if score == 2 or score == (-2):
                        modifyStrSubj = 1
                    elif score == 1 or score == (-1):
                        modifyWeakSubj = 1

                if word2 in dict:
                    score == dict[word2]
                    if score == 2 or score == (-2):
                        modifiedStrSubj = 1
                    elif score == 1 or score == (-1):
                        modifiedWeakSubj = 1

    vector = [preByAdj, preByAdv, preByIntensifier, isNegExist]
    vector = vector + [modifyStrSubj, modifyWeakSubj, modifiedStrSubj, modifiedWeakSubj]
    vector = vector + [isRcmodExist, isDepExist, iscopExist]
    # vector = vector + [isRcmodExist, rcmodScore, isDepExist, depScore, iscopExist, copScore]
    # print vector
    return vector