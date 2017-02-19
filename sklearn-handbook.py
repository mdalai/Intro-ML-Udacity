# Train test split
from sklearn.model_selection import train_test_split
X_train, y_train, X_test, y_test = train_test_split(X,y,test_size=0.20)

# Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)

# Mean absolute error
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
classifier = LinearRegression()
classifier.fit(X,y)
guesses = classifier.predict(X)
error = mean_absolute_error(y, guesses)

# R2 Score
from sklearn.metrics import r2_score
y_true =[1,2,4]
y_pred = [1.3,2.5,3.7]
r2_score(y_true,y_pred)

# K-Fold cross validation
from sklearn.model_selection import KFold
kf = KFold(12,3,shuffle=True)

for  train_indices, test_indices in kf:
	print train_indices, test_indices