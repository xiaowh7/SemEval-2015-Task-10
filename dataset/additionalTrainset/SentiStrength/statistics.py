__author__ = 'seven'
poscnt = 0
negcnt = 0
neucnt = 0
count = 0
threshold = 9000
dataset = "SentiStrength"
infile = open('%s_train_full.csv' % dataset, 'r')
trainList = infile.readlines()
outfile = open('%s_train.csv' % dataset, 'w')

inDepFile = open('%s_dependency_full.txt' % dataset, 'r')
trainDepList = inDepFile.readlines()
outDepFile = open('%s_dependency.txt' % dataset, 'w')

for i in xrange(0, len(trainList)):
    line = trainList[i]
    data = line.strip('\n').split('\t')
    sentiment = data[3]
    if sentiment == 'positive':
        poscnt += 1
        if poscnt <= threshold:
            outfile.write(line)
            outDepFile.write(trainDepList[i])
    # elif sentiment == 'neutral':
    #     neucnt += 1
    #     if neucnt <= threshold:
    #         outfile.write(line)
    elif sentiment == 'negative':
        negcnt += 1
        if negcnt <= threshold:
            outfile.write(line)
            outDepFile.write(trainDepList[i])
    count += 1

print poscnt, neucnt, negcnt, count