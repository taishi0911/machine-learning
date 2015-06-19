# coding: utf-8
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import csv

#データの格納
name_train = []
name_test = []
data_train = []
data_test = []
label_train = []

f = open('data_train02.txt','r')
for line in f:
	item = line.strip().split('\t')
	name_train.append(item.pop(0))
	label_train.append(item.pop())
	data_train.append(item)
print "教師データ:"
for i,datum in enumerate(data_train):
	print name_train[i],datum[0],datum[1],datum[2],datum[3],datum[4],datum[5],datum[6],datum[7],datum[8],datum[9],datum[10],label_train[i]

f = open('data_test02.txt','r')
for line in f:
	item = line.strip().split('\t')
	name_test.append(item.pop(0))
	data_test.append(item)
name_test.extend(name_train)
data_test.extend(data_train)
print "\nテストデータ:"
for i,datum in enumerate(data_test):
	print name_test[i],datum[0],datum[1],datum[2],datum[3],datum[4],datum[5],datum[6],datum[7],datum[8],datum[9],datum[10]
#機械学習
estimator = svm.SVC(probability=True)
estimator.fit(data_train, label_train)
label_predict = estimator.predict(data_test)
prob = 1./(1.+np.exp(-estimator.decision_function(data_test)))

#結果出力
results = []
print "\n結果:"
for i,name in enumerate(name_test):
	print name,label_predict[i],prob[i]
	temp = [name,label_predict[i],prob[i]]
	results.append(temp)
print
print
results.sort(key = lambda x: x[2])
f = open("result.csv","wb")
csvWriter = csv.writer(f)
for result in results:
	print result[0],result[1],result[2]
	csvWriter.writerow(result)
f.close()

def extract(list,i):
	array = []
	for item in list:
		array.append(item[i])
	return array

fp = FontProperties(fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf')
plt.plot(extract(data_test,0),prob,'o')
plt.xlabel(u"消極的な必要性",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標1.png")
plt.show()


plt.plot(extract(data_test,1),prob,'o')
plt.xlabel(u"積極的な必要性",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標2.png")
plt.show()

plt.plot(extract(data_test,2),prob,'o')
plt.xlabel(u"人が足りてない仕事か",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標3.png")
plt.show()

plt.plot(extract(data_test,3),prob,'o')
plt.xlabel(u"責任を伴う仕事か求人倍率",fontproperties=fp)
plt.ylabel("消える確率",fontproperties=fp)
plt.savefig("指標4.png")
plt.show()

plt.plot(extract(data_test,4),prob,'o')
plt.xlabel(u"作業が学習しやすいか",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標5.png")
plt.show()

plt.plot(extract(data_test,5),prob,'o')
plt.xlabel(u"結果に差が出ない仕事か",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標6.png")
plt.show()

plt.plot(extract(data_test,6),prob,'o')
plt.xlabel(u"特定の人物がやることに意味がある仕事か",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標7.png")
plt.show()

plt.plot(extract(data_test,7),prob,'o')
plt.xlabel(u"代替するのにかかるコスト",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標8.png")
plt.show()

plt.plot(extract(data_test,8),prob,'o')
plt.xlabel(u"今の機械にとってどれくらい代替するのが難しい仕事か",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標9.png")
plt.show()

plt.plot(extract(data_test,9),prob,'o')
plt.xlabel(u"将来の機械が能力的に代替できうるか",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標10.png")
plt.show()

plt.plot(extract(data_test,10),prob,'o')
plt.xlabel(u"機械化が起こると言れている仕事か",fontproperties=fp)
plt.ylabel(u"消える確率",fontproperties=fp)
plt.savefig("指標11.png")
plt.show()
