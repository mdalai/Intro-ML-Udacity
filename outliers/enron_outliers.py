#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
#data_dict.pop('TOTAL', 0)
#data_dict.pop('SKILLING JEFFREY K',0)
#data_dict.pop('LAY KENNETH L',0)
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

outlier = ""

print data.max(axis=0)[0] # array first column max value
for key in data_dict:
	if data_dict[key]['salary'] == data.max(axis=0)[0]:
		print key, data_dict[key]
		outlier = key

### 2. remove outlier ----
print "remove outlier and make scatter plot ..............."
#print outlier
data_dict.pop(outlier, 0)

# rerun the scatter plot
data = featureFormat(data_dict, features)
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary2")
matplotlib.pyplot.ylabel("bonus2")
matplotlib.pyplot.show()


### 3. remove more outlier ----
print "There are following outliers ......"
#outliers =[]
for key in data_dict:
	if data_dict[key]['salary'] >= 1000000.0 and data_dict[key]['bonus'] >= 5000000.0 and data_dict[key]['salary']!='NaN' and data_dict[key]['bonus']!='NaN':
		print key, data_dict[key]['salary'], data_dict[key]['bonus']
		#outliers.append(key)

#print outliers