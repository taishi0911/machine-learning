#coding=utf-8

"""
sequenceを操作するbuild-in-function
map; 全ての要素に操作を行う
filter; 全ての要素のうち条件に一致する要素のみ抽出する
reduce; 全部まとめて一つにする
sorted; 与えたリストを指定の要素でソートする

"""

items = [1,2,3,4,5,6]

#plus関数を定義してmapに渡す
def plus(n):
	return n+10
d1 = map(plus, items)
print d1

# itemsは変更されない

# 無名関数lambdaを使って書くとこうなる
d2 = map(lambda x:x+20, items)
print d2

# mapを使わずに全ての要素に操作を行う
d3 = [x+30 for x in items]
print d3

#filterで条件に一致するものを抽出する
def rest(n):
	if n%3==0:
		return True
d4=filter(rest, items)
print d4

#lambda関数を使って
d5=filter(lambda x:x%3==1, items)
print d5

#filterを使わずに条件に一致するものを取り出す
d6=[x for x in items if x%3==2]
print d6

#reduceで全部まとめて一つにする
def add_func(a,b):
	return a+b

d7=reduce(add_func, items)
print d7

#sortedで2つめの要素でソートする
lists = [(7,3),(4,5),(2,4),(5,5),(0,9)]
l1=sorted(lists, key = lambda x:x[0])
l2=sorted(lists, key = lambda x:x[1])
print l1
print l2




















