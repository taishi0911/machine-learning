# http://www.python-izm.com/contents/basis/tuple.shtml
# coding = utf8

import datetime
import sys

def gettoday():

	today = datetime.datetime.today()
	value = (today.year,today.month,today.day)

	return value

if __name__=="__main__":

	test_tuple = gettoday()

	print sys.argv
	print sys.argv[0]
	print sys.argv[1] #pythonを実行する時にpythonファイルの後ろに("hellow"とかを)付け加える

	print test_tuple
	print test_tuple[0]
	print test_tuple[1]
	print test_tuple[2]