import pandas as pd
Java = pd.read_csv("/Users/douglasmckinley/Desktop/gradSchool/GitHub/data/java_repos - data.csv", index_col=False)
Python = pd.read_csv("/Users/douglasmckinley/Desktop/gradSchool/GitHub/data/python_repos - data.csv", index_col=False)
#url,repo_name,watchers,stars,forks,commits,branches,releases,contributors,,
# 0,     1,        2,     3,    4,     5,      6,       7,        8
Jcolnames = Java.columns.values.tolist()
Pcolnames = Python.columns.values.tolist()

import matplotlib.pyplot as plt
import seaborn as sns

sns.jointplot(x=Jcolnames[5], y=Jcolnames[4], data=Java, kind="reg")
plt.show()

sns.jointplot(x=Pcolnames[5], y=Pcolnames[4], data=Python, kind="reg")
plt.show()