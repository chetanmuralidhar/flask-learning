import sqlite3

import sqlite3

connection = sqlite3.connect('src/mydata.db')
cursor = connection.cursor()

# create_tabel = "create table if not exists users(id integer primary key ,username text,password text)"
#
create_tabel = "create table if not exists item_model(id integer primary key AUTOINCREMENT,name text ,price real)"
cursor.execute(create_tabel)
#cursor.execute("select * from  ")
connection.commit()
connection.close()
# connection = sqlite3.connect('data.db')
#
# cursor = connection.cursor()
#
# create_table = "create table users (id int,username text,password text)"
# cursor.execute(create_table)
#
# user = (1,'chetan','asdf')
#
# insert_query = "insert into users values(?,?,?)"
# cursor.execute(insert_query,user)
#
# users = [
#     (2,'pawan','asdf'),
#     (3,'anna','asdf')
# ]
# cursor.executemany(insert_query,users)
#
# select_query = "select * from users"
# for row in cursor.execute(select_query):
#     print(row)
#
# connection.commit()
# connection.close()