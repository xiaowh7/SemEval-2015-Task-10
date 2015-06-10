#!/bin/bash
PROJECT_PATH=~/Twitter-Sentiment-Analysis-master/\
sentence-level-analysis
python preprocess.py \
SemEval2014-task9-test-B-gold.txt \
SemEval2014-task9-test-B-gold_reformated.txt \
tweets.txt
$PROJECT_PATH/ark-tweet-nlp/runTagger.sh tweets.txt > tweetsTagged.txt
#./dependencyParser.sh
python combine.py \
SemEval2014-task9-test-B-gold_reformated.txt \
tweetsTagged.txt \
SemEval2014_test.csv
