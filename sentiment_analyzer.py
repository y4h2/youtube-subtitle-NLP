import collections
import nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews, stopwords
from nltk.metrics import scores
from nltk import sent_tokenize, word_tokenizer
import re

stopset = set(stopwords.words('english'))

def data_clean(text):
	# split content into sencetence
	# based on the character
	# if (re.search("(\[.*\])", text)):
	# 	sentences = re.compile("(\[.*\])").split(text)
	sentences = sent_tokenize(text)
	for sentence in sentences:
		words = word_tokenizer(sentence)
	# stem the word

def evaluate_classifier(featx):
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
 
    negfeats = [(featx(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(featx(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4
 
    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
 
    classifier = NaiveBayesClassifier.train(trainfeats)
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)
 
    for i, (feats, label) in enumerate(testfeats):
            refsets[label].add(i)
            observed = classifier.classify(feats)
            testsets[observed].add(i)
 
    print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
    print 'pos precision:', scores.precision(refsets['pos'], testsets['pos'])
	print 'pos recall:', scores.recall(refsets['pos'], testsets['pos'])
	print 'pos F-measure:', scores.f_measure(refsets['pos'], testsets['pos'])
	print 'neg precision:', scores.precision(refsets['neg'], testsets['neg'])
	print 'neg recall:', scores.recall(refsets['neg'], testsets['neg'])
	print 'neg F-measure:', scores.f_measure(refsets['neg'], testsets['neg'])

    classifier.show_most_informative_features()

def predication(text):
