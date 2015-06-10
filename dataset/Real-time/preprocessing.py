__author__ = 'seven'
import re
import langdetector

def preprocess():

    infile = open('fullDataUsedForPaper.txt', 'r')
    outfile = open('raw.csv', 'w')
    # outfile1 = open('tweets.csv', 'w')
    isFirst = True
    for line in infile.readlines():
        if isFirst:
            isFirst = False
            continue
        sentiment = 'neural'
        line = line.strip('\n').split('\t')
        if line[0] == '1':
            sentiment = 'positive'
        elif line[0] == '0':
            sentiment = 'neutral'
        elif line[0] == '-1':
            sentiment = 'negative'
        tweetID = line[1]
        userID = line[2]
        tweet = line[6]
        chk = re.match(r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$', tweet)
        if not chk:
            tweet = ''
        if not tweet == '':
            if langdetector.detect_language(tweet) == 'english':
                outfile.write('%s\t%s\t%s\t%s\n' % (tweetID, userID, sentiment, tweet))
            # outfile1.write('%s\n' % tweet)

    infile.close()
    outfile.close()
    # outfile1.close()

def extractTweets():
    infile1 = open('train.csv', 'r')
    outfile1 = open('train_tweets.csv', 'w')
    for line in infile1.readlines():
        line = line.split('\t')[3]
        outfile1.write(line)

    infile2 = open('Real-time_gold.csv', 'r')
    outfile2 = open('test_tweets.csv', 'w')
    for line in infile2.readlines():
        line = line.split('\t')[3]
        outfile2.write(line)

if __name__ == '__main__':
    # preprocess()
    extractTweets()