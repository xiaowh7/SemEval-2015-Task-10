__author__ = 'seven'
__author__ = 'seven'
import re
import csv

import langdetector


infile = open('IT_corpus.csv', 'r')
csvreader = csv.reader(infile, delimiter=',', quotechar='"')
outfile = open('raw.csv', 'w')
outfile1 = open('tweets.csv', 'w')
isFirst = True
cnt = 0
for line in csvreader:
    if isFirst:
        isFirst = False
        continue
    sentiment = 'neutral'
    [brand, sentiment, tweetID, time, tweet] = line
    # print brand, sentiment, tweetID, time, tweet
    if sentiment == 'irrelevant':
        continue
    # print tweet
    chk = re.match(r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$', tweet)
    if not chk:
        tweet = ''
    if not tweet == '':
        if langdetector.detect_language(tweet) == 'english':
            cnt += 1
            # tweetID = cnt
            userID = cnt
            outfile.write('%s\t%s\t%s\t%s\n' % (tweetID, userID, sentiment, tweet))
            outfile1.write('%s\n' % tweet)