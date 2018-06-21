import pymysql


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql', db='movie_db', charset="utf8")
cursor = conn.cursor()
sql_select = "select * from imdb_info where imdb_id='tt0100112'"
cursor.execute(sql_select)
info = cursor.fetchall()
print(info)





