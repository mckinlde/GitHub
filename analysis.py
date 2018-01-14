## okay I have a bunch of data let's draw regressions just for fun
import numpy as np
sample = np.loadtxt("/Users/studentuser/Desktop/Data/version2/users")

print("LINEAR REGRESSION")
import pandas as pd
D = pd.read_csv("/Users/studentuser/Desktop/Data/version2/users", index_col=False)
colnames = D.columns.values.tolist()
Y = D[colnames[0]] #total forks for a user
X = D[colnames[1:14]] #all other columns besides username
from sklearn import linear_model
regr = linear_model.LinearRegression(fit_intercept=True).fit(X, Y)
print("R^2=%0.3f" % regr.score(X, Y))
print(f"intercept and coeff: {regr.intercept_} {regr.coef_}")


print("SUPERVISED LEARNING")
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

classifier = RandomForestClassifier()
ttlaccuracy = np.mean(cross_val_score(classifier, X, Y, scoring='accuracy', cv=10))
f1accuracy = np.mean(cross_val_score(classifier, X, Y, scoring='f1_micro', cv=10))
print("Cross-validation accuracy: %0.2f" % ttlaccuracy)
print("Cross-validation F1: %0.2f" % f1accuracy)