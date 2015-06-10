__author__ = 'seven'
goldFile = open("../dataset/Semeval2013_gold.csv", 'r')
gold = []
for line in goldFile.readlines():
    gold.append(line.strip('\r\n').split('\t'))

predfile = open("./Semeval-sms_ans.txt", 'r')
pred = []
for line in predfile.readlines():
    pred.append(line.strip('\r\n').split('\t'))

ans = dict()
cnt = 0
for i in range(len(gold)):
    goldSentiment = gold[i][2]
    predSentiment = pred[i][2]
    if not goldSentiment == predSentiment:
        cnt += 1
        type = "%s -> %s" % (goldSentiment, predSentiment)
        if type in ans:
            ans[type].append([i, gold[i][3]])
        else:
            ans[type] = [[i, gold[i][3]]]

print cnt

outfile = open("error_Analysis.txt", "w")
for type in ans:
    outfile.write("%s\n", type)
    for each in ans[type]:
        outfile.write("Index: %s, Text: %s\n" % (each[0], each[1]))
    outfile.write("\n")