TEST dataset for SemEval-2015 Task #10: Sentiment Analysis on Twitter

Version 1.0: December 15, 2014

Task organizers:

Sara Rosenthal, Columbia University
Alan Ritter, The Ohio State University
Veselin Stoyanov, Facebook
Svetlana Kiritchenko, NRC Canada
Saif Mohammad, NRC Canada
Preslav Nakov, Qatar Computing Research Institute


NOTE

Please note that by downloading the Twitter data you agree to abide
by the Twitter terms of service (https://twitter.com/tos),
and in particular you agree not to redistribute the data
and to delete tweets that are marked deleted in the future.
You MUST NOT re-distribute the tweets, the annotations or the corpus obtained,
as this violates the Twitter Terms of Use.



SUMMARY

SUBTASK A:
SemEval2015-task10-test-A-input.txt          -- test input for subtask A (new data)
SemEval2015-task10-test-A-input-progress.txt -- test input for subtask A (progress test)

SUBTASK B:
SemEval2015-task10-test-B-input.txt           -- test input for subtask B (new data)
SemEval2015-task10-test-B-input-progress.txt  -- test input for subtask B (progress test)

SUBTASK C:
SemEval2015-task10-test-CD-input.txt          -- test input for subtask C (new data)

SUBTASK D:
SemEval2015-task10-test-CD-input.txt          -- test input for subtasks C and D (new data)
SemEval2015-task10-test-D-input.txt           -- test input for subtask D (new data)


IMPORTANT

In order to use these test datasets, the participants need (1), and most likely also (2) and (3):

1. the official scorers and format checkers
2. the training datasets
3. the dev datasets (CANNOT be used for training!!! Only for development!!!)

You can find them here: http://alt.qcri.org/semeval2015/task10/index.php?id=data-and-tools

The format checkers released should be used to check the output before submitting the results.

Note that the devsets CANNOT be used for training!!!



INPUT DATA FORMAT


-----------------------SUBTASK A-----------------------------------------
--Test Data--

The format for the test input file is as follows:
id1<TAB>id2<TAB>start_token<TAB>end_token<TAB>unknwn<TAB>tweet_text

for example:
NA      15115101        2       2       unknwn  amoure wins oscar
NA      15115101        3       4       unknwn  who's a master brogramer now?

--System Output--
We expect the following format for the prediction file:
id1<TAB>id2<TAB>start_token<TAB>end_token<TAB>predicted_sentiment_4_phrase<TAB>tweet_text

where tweet_text is optional,
and predicted_sentiment_4_phrase can be "positive", "negative" or "neutral".
For example:
NA      15115101        2       2       positive  amoure wins oscar
NA      15115101        3       4       neutral  who's a master brogramer now?


--Gold Standard--
The gold standard will follow the same format as the example system output above.


-----------------------TASK B-----------------------------------------
(Task B uses the same format as Task A, but it excludes the start and end token fields.)
--Test Data--

The format for the test input file is as follows:
id1<TAB>id2<TAB>unknwn<TAB>tweet_text

for example:
NA      15115101       unknwn  amoure wins oscar
NA      15115101       unknwn  who's a master brogramer now?

--System Output--
We expect the following format for the prediction file:
id1<TAB>id2<TAB>predicted_sentiment_4_tweet<TAB>tweet_text

where tweet_text is optional,
and predicted_sentiment_4_tweet can be "positive", "negative" or "neutral".
For example:
NA      15115101        positive  amoure wins oscar
NA      15115101        neutral  who's a master brogramer now?

--Gold Standard--
The gold standard will follow the same format as the example system output above.


-----------------------SUBTASK C-----------------------------------------
--Test Data--

The format for the test file is as follows:
id1<TAB>id2<TAB>unknwn<TAB>topic<TAB>tweet_text

for example:
NA      T15113803      unknwn     aaron rodgers       I just cut a 25 second audio clip of Aaron Rodgers talking about Jordy Nelson's grandma's pies. Happy Thursday.
NA      T15113805      unknwn     aaron rodgers       Tough loss for the Dolphins last Sunday in Miami against Aaron Rodgers &amp; the Green Bay Packers: 27-24.

--System Output--
We expect the following format for the prediction file:
id1<TAB>id2<TAB>predicted_sentiment_4_topic<TAB>topic<TAB>tweet_text

where tweet_text is optional,
and predicted_sentiment_4_topic can be "positive", "negative" or "neutral".
For example:
NA      T15113803      positive     aaron rodgers       I just cut a 25 second audio clip of Aaron Rodgers talking about Jordy Nelson's grandma's pies. Happy Thursday.
NA      T15113805      neutral     aaron rodgers       Tough loss for the Dolphins last Sunday in Miami against Aaron Rodgers &amp; the Green Bay Packers: 27-24.


-----------------------SUBTASK D-----------------------------------------
--Test Data--

The format for the test file is as follows:
topic<TAB>unknwn

for example:
aaron rodgers	unknwn
aaron samuels	unknwn

--System Output--
We expect the following format for the prediction file:
topic<TAB>predicted_POS_to_POS+NEG_ratio

Where predicted_POS_to_POS+NEG_ratio should be a number between 0 and 1,
representing a prediction for the positive/(positive+negative) ratio
for the sentiment of the tweets for the given topic.

For example:
aaron rodgers	0.8125
aaron samuels	0.176470588

Note that the tweets for a given topic can be found in the file for subtask C.
-------------------------------------------------------------------------


-----------------------SUBTASK E-----------------------------------------
Data released separately; see http://alt.qcri.org/semeval2015/task10/
-------------------------------------------------------------------------


INPUT DATA FORMAT NOTES

1. For subtask A, the annotations are at the token level, where the tokenization is on a single " " (space). Note that in the case of two consecutive spaces, this creates an empty token, which is counted! Also, note that token counting starts from zero.

2. Some characters are escaped in the progress test input (but not in the new data), e.g.,

@BarackObama\u002c Clinton\u002c Panetta\u002c Petraeus we will not #StandDown on Nov 6 or Nov 7 or Nov 8th. Do the right thing now. #WeWillNotLetThisGo



EVALUATION

For subtasks A, B, and C, the metric for evaluating the participants' systems will be average F1-measure (averaged F1-positive and F1-negative, and ignoring F1-neutral; note that this does not make the task binary!), as well as F1-measure for each sentiment class (positive, negative, neutral), which can be illuminating when comparing the performance of different systems.
For each subtask, the systems will be ranked based on their average F1-measure.

For subtask D, we will score the POS/(POS+NEG) ratio in two ways:
(a) How close it is to the gold ratio.
(b) How well these scores perform when mapped to coarse categories: strongly positive, weakly positive, mixed, weakly negative, and strongly negative. We define these categories as follows:
- strongly positive: 80% < POS/(POS+NEG) <= 100%
- weakly positive:   60% < POS/(POS+NEG) <= 80%
- mixed:             40% < POS/(POS+NEG) <= 60%
- weakly negative:   20% < POS/(POS+NEG) <= 40%
- strongly negative:  0% <=POS/(POS+NEG) <= 20%

See also the scorers for details on scoring the output:
http://alt.qcri.org/semeval2015/task10/index.php?id=data-and-tools

Note that for subtasks A and B, we have two test inputs, as we have progress tests.


DATASET USE

The development datasets are intended to be used as a development-time evaluation dataset as the participants develop their systems. However, devsets CANNOT be used for training!!!


TEAMS

We discourage multiple teams with overlapping team members.


SUBMISSION NOTES

1. Participants must submit their runs by the final deadline of December 22, 2014 (23:59 at Midway, Midway Islands, United States: see http://www.timeanddate.com/worldclock/city.html?n=1890). Late submissions will not be counted.

2. Participants can make new submissions, which will substitute their earlier submissions on the Web server multiple times, but only before the deadline (see above). Thus, we advise that participants submit their runs early, and possibly resubmit later if there is time for that. Only the last submission that was also on time will be counted.

3.  Participants are free to use any data: we will not distinguish between closed (that only use the provided data) and open (that also use additional data) runs. However, they will need to describe the resources and tools they have used to train their systems in the Web form they have recieved by email.



SUBMISSION PROCEDURE

1. Instructions on how to upload a submission and how to fill in a form with a system's description are sent by email when registering for test data download.

2. Each team's submission can include runs for any of the four subtasks (A, B, C, and D; subtask E is handled separately). When a team participates in subtask A or/and B, then submission is required for both the new data and for the progress test.

3. For *each task*, a team may submit a *single* run, as this year, we make no distinction between closed (constrained) and open (unconstrained) runs.

4. Format of the submission: a single ZIP file should contain two files *for each subtask*

- GROUP-SUBTASK.output
- GROUP-SUBTASK.description

Where GROUP is the group name, and SUBTASK is "A", "B", "C" or "D".
For example: "QCRI-A.output" + "QCRI-A.description".

The first file should follow the output format specified above for the respective subtask.

The second file should have the format of the SUBMISSION_DESCRIPTION_TEMPLATE.txt.
It should contain the following information:

	1. Team ID

	2. Team affiliation

	3. Contact information

	4. Submission, i.e., ZIP file name

	5. System specs

	- 5.1 Core approach

	- 5.2 Supervised or unsupervised

	- 5.3 Critical features used

	- 5.4 Critical tools used

	- 5.5 Significant data pre/post-processing

	- 5.6 Other data used (outside of the provided)

	- 5.7 Size of the training Twitter data used (some teams could only download part of the data)

	- 5.8 Did you participate in SemEval-2013 task 2?

	- 5.9 Did you participate in SemEval-2014 task 9?

	6 References (if applicable)



LICENSE

The accompanying dataset is released under a Creative Commons Attribution 3.0 Unported License
(http://creativecommons.org/licenses/by/3.0/).


CITATION

You can cite the folowing paper when referring to the dataset:

@InProceedings{Rosenthal-EtAl:2015:SemEval,
  author    = {Sara Rosenthal and Alan Ritter and Veselin Stoyanov and Svetlana Kiritchenko and Saif Mohammad and Preslav Nakov},
  title     = {SemEval-2015 Task 10: Sentiment Analysis in Twitter},
  booktitle = {Proceedings of the 9th International Workshop on Semantic Evaluation (SemEval 2015)},
  year      = {2015},
  publisher = {Association for Computational Linguistics},
}



USEFUL LINKS:

Google group: semevaltweet@googlegroups.com
SemEval-2015 Task 10 website: http://alt.qcri.org/semeval2015/task10/
SemEval-2015 website: http://alt.qcri.org/semeval2015/


