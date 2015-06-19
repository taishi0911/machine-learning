# -*- coding:utf-8 -*-

print "処理開始"

try:
	print "try-開始"
	a = 10/0
	print "try-終了"

except:
	print "エラー発生"

print "処理終了"