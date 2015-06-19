#coding: utf8
data = [
	{"name":"田中花子","gender":"女性","score":"58","birthyear":"1980"},
	{"name":"鈴木一郎","gender":"男性","score":"70","birthyear":"2000"},
	{"name":"山田太郎","gender":"男性","score":"46","birthyear":"1989"},
	{"name":"佐藤恵子","gender":"女性","score":"89","birthyear":"1992"},
	{"name":"石井あや","gender":"女性","score":"60","birthyear":"1978"}
	]

def judge(x):
	if x%400==0:
		return True
	elif x%100!=0 and x%4==0:
		return True
	else:
		return False

leapyear_score=0
leapyear_number=0
non_leapyear_score=0
non_leapyear_number=0


for datum in data:
	if judge(int(datum["birthyear"])) is True:
		leapyear_score=leapyear_score+int(datum["score"])
		leapyear_number=leapyear_number+1		
	elif judge(int(datum["birthyear"])) is False:
		non_leapyear_score=non_leapyear_score+int(datum["score"])
		non_leapyear_number=non_leapyear_number+1

		
leapyear_mean=leapyear_score/leapyear_number
print "閏年の人の平均スコア"
print leapyear_mean

non_leapyear_mean=non_leapyear_score/non_leapyear_number
print "閏年ではない人の平均スコア"
print non_leapyear_mean
