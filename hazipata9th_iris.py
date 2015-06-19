# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn import datasets

#データセットの読み込み
iris = datasets.load_iris()
X = iris.data
Y = iris.target

###主成分分析

#共分散行列を求める。x.transposeで転置してベクトルにする。np.dotで内積が出る。
#".T"でもtransposeと同じ。X.shape[0]は表の縦軸を示す。X.shape[1]は表の横軸を示す。

X_bar = np.array([row - np.mean(row) for row in X.transpose()]).transpose()
m = np.dot(X_bar.T, X_bar) / X.shape[0]

#固有値(eigenvalue)問題を解く。np.linalg.eig(A)で出る。
(w, v) = np.linalg.eig(m)
v = v.T

#固有値の大きい順に固有値と固有ベクトルをソート
tmp = {}
for i, value in enumerate(w):
	tmp[value] = i

v_sorted = []
for key in sorted(tmp.keys(), reverse=True):
	v_sorted.append(v[tmp[key]])
v_sorted = np.array(v_sorted)

w_sorted = np.array(sorted(w, reverse=True))

#固有値のグラフと累積寄与率のグラフを描く

x = [1, 2, 3, 4]
plt.bar(x, w_sorted, align="center")
plt.xticks(x, ["1","2","3", "4"]) 
plt.show()

w_total = 0
for i in range(4):
	w_total = w_total + w_sorted[i]

r = [0, 0, 0, 0]

for j in range(4):
	c_j = 0
	for k in range(j+1):
		c_j = c_j + w_sorted[k]
		r[j] = c_j/w_total

x = [1, 2, 3, 4]
plt.bar(x, r, align="center")
plt.xticks(x, ["1","2","3", "4"]) 
plt.show()