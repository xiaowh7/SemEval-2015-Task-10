__author__ = 'seven'
inFile = open('raw.csv', 'r')
count = 0
poscnt = 0
negcnt = 0
neucnt = 0
postest = 0
neutest = 0
negtest = 0
threshold = 900
outFile = open('train.csv', 'w')
testFile = open('Real-time_gold.csv', 'w')
for line in inFile.readlines():
    data = line.split('\t')
    count += 1
    sentiment = data[2]
    if sentiment == 'positive':
        poscnt += 1
        if poscnt <= threshold:
            outFile.write("%s" % line)
        else:
            postest += 1
            testFile.write("%s" % line)
    elif sentiment == 'neutral':
        neucnt += 1
        if neucnt <= threshold:
            outFile.write("%s" % line)
        else:
            neutest += 1
            testFile.write("%s" % line)
    elif sentiment == 'negative':
        negcnt += 1
        if negcnt <= threshold:
            outFile.write("%s" % line)
        else:
            negtest += 1
            testFile.write("%s" % line)

print poscnt, neucnt, negcnt, count
print postest, neutest, negtest, postest+negtest+negtest