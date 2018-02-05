
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tflearn


D = pd.read_csv("/Users/douglasmckinley/Downloads/Basic_GitHub_TFLearn - Sheet1.csv", index_col=False)
colnames = D.columns.values.tolist()
import tflearn
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# /// load a CSV for tflearn linear regression: all cols are floats, and the 0th column is the target
X, Y = tflearn.data_utils.load_csv("/Users/douglasmckinley/Downloads/forks_TFLearn - users.csv", target_column=0)
X = np.array(X, dtype=np.float32)  # convert to floats
Y = np.array(Y, dtype=np.float32)
Y = [[v] for v in Y]  # reorganize [y1, y2, y3, ...] to [[y1], [y2], [y3], ...] for compatibility w/ TFlearn library
print("loaded %i data points" % len(X))

# /// perform linear regression of Y on X
nfeatures = len(X[0])  # equals the number of columns we're using to make predictions
noutputs = len(Y[0])  # equals the number of columns we're trying to predict, i.e., 1 in this case
inputs = tflearn.input_data(shape=[None, nfeatures])
linear_combo = tflearn.fully_connected(inputs, noutputs, activation='linear')  # linear combination of inputs
# finally, construct and run a deep neural net (DNN) that will do simple-gradient-descent (sgd) on mean_square,
# selecting optimal models based on how well they maximize R^2
regression = tflearn.regression(linear_combo, optimizer='sgd', loss='mean_square', metric='R2', learning_rate=0.01)
model = tflearn.DNN(regression)
model.fit(X, Y, n_epoch=1000, show_metric=True, snapshot_epoch=False)

