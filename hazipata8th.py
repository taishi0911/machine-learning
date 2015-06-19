#coding: UTF-8
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt


train_num = 100
d1_x = np.random.rand(train_num/2)*5+1
d1_y = np.random.rand(train_num/2)*5+1
label_d1 = np.ones(train_num/2)

d2_x = (np.random.rand(train_num/2)*5+1)*-1
d2_y = (np.random.rand(train_num/2)*5+1)*-1
label_d2 = np.ones(train_num/2)*0

d1 = np.c_[d1_x, d1_y]
d2 = np.c_[d2_x, d2_y]

d = np.vstack((d1,d2))
L = np.r_[label_d1,label_d2]

clf = svm.SVC(kernel="linear", C = 1.0)
clf.fit(d,L)

w = clf.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(-8,8)
yy = a*xx-clf.intercept_[0]/w[1]

plt.scatter(d1[:,0],d1[:,1],c = "red", marker = "o")
plt.scatter(d2[:,0],d2[:,1],c = "yellow", marker = "o")
plt.plot(xx,yy)
plt.show()