__author__ = 'seven'
# decode = {1.0: 'positive', 2.0: 'negative', 3.0: 'neutral'}
# testlabel = [1.0, 2.0, 3.0, 2.0, 1.0]
# data1 = []
# encode = {'positive': 1.0, 'negative': 2.0, 'neutral': 3.0}
# for i in range(len(testlabel)):
# givenLabel = testlabel[i]
#     label = decode[givenLabel]
#     data1.append(label)
# print data1
# print len(testlabel)
# a = range(0, 10)
# print type(a)
# print a
# print a[0], a[1]
# print "##########################"
# a = xrange(0, 10)
# print type(a)
# print a
# print a[0], a[1], a[1]
# def output(dataset, predictLabel):
#     goldFilename = "..//SemEval2014-task9-scoring-script//" \
#                    "SemEval2014-task9-test-B-gold.txt"
#     predFilename = "../result//%s.pred" % dataset
#     goldFile = open(goldFilename, 'r')
#     predFile = open(predFilename, 'w')
#
#     index = 0
#     for line in goldFile:
#         data = line.strip("\r\n").split("\t")
#         predFile.write("%s\t%d\t%s\n" % (data[0], index+1, predictLabel[index]))
#         index += 1
#
#     goldFile.close()
#     predFile.close()
#
#

# output("Semeval", predictLable)
# from output import *
# dataset = "Twitter-2013"
# predFilename = "../dataset/SemEval2014-Task9/%s/%s_pred.csv" \
#                % (dataset, dataset)
# goldFilename = "../dataset/SemEval2014-Task9/Twitter-2013/" \
#                "Twitter-2013_gold.csv"
# predictLabel = []
# f = open("taskB.pred", 'r')
# for line in f:
#     predictLabel.append(line.strip("\r\n"))
# Semeval2013Output(predictLabel, goldFilename, predFilename)
# import re
# ans = re.findall(r'\d+', 'Twitter-2013')
# print ans
# ans = raw_input("train required? (y/n):")
# print ans
l = [1, 4, 6, 7, 9, 12]
for i in xrange(3, len(l)):
    print l[i]