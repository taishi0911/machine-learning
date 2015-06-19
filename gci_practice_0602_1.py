#coding: utf8
import MySQLdb
import config

dbcon = mysql.connector.connect(
	databese='twitter',
	user='taishiokano',
	password='taishi0911',
	host='127.0.0.1'
	)
dbcur=dbcon.cursor()

user_id=1234567
dbcur.execute('''select tweet_id, text, created_at from tweets where user_id=%s ''',(user_id,))
for row in dbcur.fetchall():
	print row