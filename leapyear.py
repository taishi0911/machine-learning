#coding:utf8
#for i in range(1900, 2200):
#	if i%400 == 0:
#		print "閏年"
#	elif i%100!=0 and i%4 == 0:
#		print "閏年"
#	else:
#		print i

print "下記の年は閏年です"

leapyear=[]
for i in range(1900, 2200):
	if i%400 == 0:
		leapyear.append(i)
	elif i%100!=0 and i%4 == 0:
		leapyear.append(i)
print leapyear