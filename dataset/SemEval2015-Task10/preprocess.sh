#!/bin/bash
PROJECT_PATH=~/SemEval-Task9-master
python preprocess.py \
SemEval2015-task10-test-B-input.txt tweets.txt
$PROJECT_PATH/ark-tweet-nlp/runTagger.sh tweets.txt > tweetsTagged.txt
#./dependencyParser.sh
python combine.py \
SemEval2015-task10-test-B-input.txt \
tweetsTagged.txt \
SemEval2015_test.csv