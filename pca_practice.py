# -*- coding: utf-8 -*-

import numpy as numpy
import matplotlib
import matplotlib.pyplot as plt

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target

#X_bar = np.array([row - np.mean(row) for row in X.transpose()]).transpose()
#m = np.doc(X_bar.T, X_bar) / X.shape[0]

print X.shape[0]
print X.shape[1]
#print X.shape[2]
#print X.shape[3]
print X.shape

#(w, v) = np.linalg.eig(m)
#v = v.T