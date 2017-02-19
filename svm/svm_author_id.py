#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#### 1% of data
#features_train = features_train[:len(features_train)/100]
#print(features_train)
#labels_train = labels_train[:len(labels_train)/100]
#print(labels_train)

#########################################################
### your code goes here ###
from sklearn.svm import SVC
#clf = SVC(kernel='linear')
#clf=SVC(kernel='rbf')  # acc = 0.616
#clf=SVC(kernel='rbf', C=10.)  # acc = 0.616
#clf=SVC(kernel='rbf', C=100.)  # acc = 0.616
#clf=SVC(kernel='rbf', C=1000.)  # acc = 0.821
clf=SVC(kernel='rbf', C=10000.0)  # acc= 0.892
t0 = time()
clf.fit(features_train,labels_train)
print"training time:",round(time()-t0,3),"s"
t0 = time()
pred = clf.predict(features_test)
print(pred.size)
print(np.count_nonzero(pred)) #877

print"predicting time:",round(time()-t0,3),"s"
print(pred[10],pred[26],pred[50])

accuracy = clf.score(features_test, labels_test)
print(accuracy)

#########################################################


