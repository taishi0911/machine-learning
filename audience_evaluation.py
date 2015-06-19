#coding: utf8
data = [
	{"name":"田中花子","gender":"女性","score":"58"},
	{"name":"鈴木一郎","gender":"男性","score":"70"},
	{"name":"山田太郎","gender":"男性","score":"46"},
	{"name":"佐藤恵子","gender":"女性","score":"89"},
	{"name":"石井あや","gender":"女性","score":"60"}
	]

male = 0
female = 0
for datum in data:
	if datum["gender"]=="男性":
		male = male +1
	else:
		male = male
	if datum["gender"]=="女性":
		female = female +1
	else:
		female = female
print male, female

total = 0
for derum in data:
	total = total + int(datum["score"])
mean = total / len(data)
print mean
