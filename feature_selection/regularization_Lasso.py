
# Lasso Regression
import sklearn.linear_model.Lasso
features, labels = GetMyData()
regression = Lasso()
regression.fit(features,labels)
regression.predict([[2,4]])

regression.coef_
regression.intercept_