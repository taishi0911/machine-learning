import mysql.connector

config = {
  'user': 'taishiokano',
  'password': 'taishi0911',
  'host': '127.0.0.1',
  'database': 'twitter',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cnx.close()