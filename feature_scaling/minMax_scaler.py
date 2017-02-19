from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.],[140.],[175.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print rescaled_weight


import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )  # dictionary to array Numpy
poi, finance_features = targetFeatureSplit( data )

from sklearn.preprocessing import MinMaxScaler
import numpy as np
min_max_scaler = MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(finance_features)
#print X_train_minmax44
X_test = np.array([[200000., 1000000.]])
X_test_minmax = min_max_scaler.transform(X_test)
print "Testing feature scalling: ", X_test_minmax

