## Take in CSV file, columns w/headers
## Automatically draw all possible regression lines
## Sort by highest R^2
## Display in order


import pandas as pd
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tflearn

D = pd.read_csv("/Users/douglasmckinley/Downloads/forks_TFLearn - users.csv", index_col=False)
colnames = D.columns.values.tolist()

def loadTargets():
    targetCol = D[colnames[0]]
    targetCol.value = targetCol.round()

    if targetCol.min() != 0:
        print("Error: the minimum class value should be 0")
        exit(-1)
    C = targetCol.max()
    if C <= 0:
        print("Error: the maximum class value should be greater than 1")
        exit(-1)

    N = len(targetCol)

    targets = np.zeros((N, C + 1))
    # print(targetCol)
    for i in range(0, N):
        targets[i][targetCol[i]] = 1
    # print(targets)
    return targets


def loadFeatures():
    # print(colnames[1:])
    featureCols = D[colnames[1:]]
    return featureCols.values


targets = loadTargets()
features = loadFeatures()

if len(targets) != len(features):
    print("Error: Number of targets doesn't match number of feature rows")
    exit(-1)

net = tflearn.input_data(shape=[None, len(features[0])])  # tells how many features we have, i.e., the shape of inputs
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, len(targets[0]), activation='softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net)

model.fit(features, targets, n_epoch=10, batch_size=16, validation_set=(features, targets), show_metric=True)

for i in range(len(features)):
  user = features[i]
  print(targets[i], " vs ", model.predict([user]))
