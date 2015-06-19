__author__='taishiokano'

# coding: utf8
import mysql.connector
import config

dbcon = mysql.connector.connect(
	databese='twitter',
	user='taishiokano',
	password='taishi0911',
	host='127.0.0.1'
	)
