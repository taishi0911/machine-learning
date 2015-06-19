import mysql.connector
 
config = {
    'user': 'YOUR_ID',
    'password': 'YOUR_PASSWORD',
    'host': '******.ap-northeast-1.rds.amazonaws.com'
}
 
cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)
sql = "select * from TABLE"
cur.execute(sql)
 
#DATE, VALUE
for (DATE, VALUE) in cur:
    print(DATE, VALUE)
 
cur.close()
cnx.close()