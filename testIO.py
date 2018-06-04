import pymysql


db=pymysql.connect(host="localhost",user="Rooobins",password="19910909kai",db="spiderData",port=3306)



cursor=db.cursor()

cursor.execute("select * from spotData limit 100")

data=cursor.fetchone()

print("database version : %s "% data)

db.close()

