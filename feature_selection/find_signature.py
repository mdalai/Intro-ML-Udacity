#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
#words_file = "../tools/word_data.pkl" 
#authors_file = "../tools/email_authors.pkl"
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
#vectorizer = TfidfVectorizer(stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()



### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)
accuracy = clf.score(features_test,labels_test)
print "Accuracy is ", accuracy  #0.94

feature_no_imp = 0
for i in range(len(clf.feature_importances_)):
	if clf.feature_importances_[i] >= 0.2:
		print "The most importance is ", clf.feature_importances_[i]
		print "The feature # of most importance is ", i    # 1st time 34058, 2nd 14412, 3rd 21458
		feature_no_imp = i



### Accuracy 1.0 on overfit data
importances = clf.feature_importances_
import numpy as np
indices = np.argsort(importances)[::-1]
print 'Feature Ranking: '
for i in range(10):
    print "{} feature no.{} ({})".format(i+1,indices[i],importances[indices[i]])

    
#print f_im for f_im in clf.feature_importances_ if f_im >= 0.2 

print "The most important word is ---- ", vectorizer.get_feature_names()[feature_no_imp]



