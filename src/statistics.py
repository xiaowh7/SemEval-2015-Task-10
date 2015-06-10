__author__ = 'seven'
smsFilename = "..//dataset//SemEval2013-Task2B//sms//sms-Semeval2013_gold.csv"
file = open(smsFilename, 'r')
sms = {}
for line in file:
    data = line.strip('\r\n').split('\t')
    index = data[0]
    sentiment = data[2]
    sms[index] = sentiment

file.close()



goldFilename = "..//dataset//SemEval2014-Task9//" \
                   "SemEval2014-task9-test-B-gold_reformated.txt"
file = open(goldFilename, 'r')
poscnt = 0
negcnt = 0
neucnt = 0
count = 0
bingo = 0
for line in file.readlines():
    data = line.strip('\r\n').split('\t')
    index = data[0]
    source = data[1]
    if source.startswith("SM"):
        sentiment = data[2]
        if sentiment == sms[index]:
            bingo += 1
            sms[index] = "test"
        if sentiment == 'positive':
            poscnt += 1
        elif sentiment == 'neutral':
            neucnt += 1
        elif sentiment == 'negative':
            negcnt += 1
        count += 1

for key in sms:
    if not sms[key] == "test":
        print key
print poscnt, neucnt, negcnt, bingo, count