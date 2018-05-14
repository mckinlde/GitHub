import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import matplotlib.pyplot as plt

# /// Read CSV into DataFrame, labeling columns with headers, not specifying a column (index_col) to label each row
D = pd.read_csv("/Users/douglasmckinley/Desktop/gradSchool/GitHub/data/Python_Java - github.csv", index_col=False)
print(D.head())
#[       0,    1,    2,      3,       4,       5,           6,     7,           8,        9,       10,         11,          12,          13,              14,        15]
# watchers,stars,forks,commits,branches,releases,contributors,Python,NormWatchers,NormStars,NormForks,NormCommits,NormBranches,NormReleases,NormContributors,Popularity
# 239,4847,1728,79,1,0,16,1,-0.1370621704,0.1171387806,0.4430149376,-0.4454480882,-0.540516547,-0.4127248364,-0.3166143717,0.1410305159
# 297,4096,268,241,2,27,20,1,0.03136860248,-0.05660658313,-0.5521336845,0.2272792926,-0.5365636377,0.3377329531,-0.2652639929,-0.1924572217
# 172,2957,364,1,59,6,0,1,-0.3316287528,-0.3201165289,-0.4866992546,-0.7693538642,-0.3112478077,-0.2459564388,-0.5220158868,-0.3794815121



# /// Treat 1st column as thing to predict (dependent var), and other columns as predictors (independent variables)
colnames = D.columns.values.tolist()
Y = D[colnames[15]]
X = D[colnames[11:14]]

# /// Approach #1: Just do a linear regression and output the R^2 score, as well as the coefficients
regr = linear_model.LinearRegression(fit_intercept=True).fit(X, Y)
print("R^2=%0.3f" % regr.score(X, Y))
print(f"intercept and coeff: {regr.intercept_} {regr.coef_}")

# /// Approach #2: Do the linear regression and compute P values and quality statistics
XwithIntercept = sm.add_constant(X)
model = sm.OLS(Y, XwithIntercept).fit()
print(model.summary())

# /// Plot the predicted values as a function of the actual values
plt.scatter(Y, regr.predict(X))
plt.xlabel('actual')
plt.ylabel('predicted')
plt.show()
