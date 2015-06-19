#coding: utf8
def judge(x):
	if x%400==0:
		print "閏年です"
	elif x%100!=0 and x%4==0:
		print "閏年です"
	else:
		print "閏年ではありません"

i=input()
judge(i)
