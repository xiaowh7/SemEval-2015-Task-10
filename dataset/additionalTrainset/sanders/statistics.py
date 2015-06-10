__author__ = 'seven'
file = open('test_final.csv', 'r')
poscnt = 0
negcnt = 0
neucnt = 0
count = 0
threshold = 500
outfile = open('balanced.csv', 'w')
for line in file.readlines():
    data = line.strip('\n').split('\t')
    sentiment = data[3]
    if sentiment == 'positive':
        poscnt += 1
        if poscnt <= threshold:
            outfile.write(line)
    # elif sentiment == 'neutral':
    #     neucnt += 1
    #     if neucnt <= threshold:
    #         outfile.write(line)
    elif sentiment == 'negative':
        negcnt += 1
        if negcnt <= threshold:
            outfile.write(line)
    count += 1

print poscnt, neucnt, negcnt, count