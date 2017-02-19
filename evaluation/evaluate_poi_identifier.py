#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)
acc = clf.score(features_test, labels_test)
print "The accuracy after cross validation: ", acc

pred = clf.predict(features_test)
print "Count predicted POIs: ",numpy.count_nonzero(pred)
print "Total predictions: ", len(pred)

Total_0_labels = sum(1 for ii in labels_test if ii==0.0)
print "Total 0 labels in test set: ", Total_0_labels, float(Total_0_labels)/float(len(pred))

pred = pred.tolist() # numpy array to list

count = 0
for i in range(len(pred)):
	if pred[i] == labels_test[i] and pred[i] == 1.0: # true positive
		count += 1
print "True positive count: ", count

### Precision and Recall
from sklearn.metrics import precision_score, recall_score
p_score = precision_score(labels_test,pred)
print "Precision Score: ", p_score
r_score = recall_score(labels_test,pred)
print "Recall Score: ", r_score
