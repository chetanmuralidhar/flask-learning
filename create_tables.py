import sqlite3

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

create_tabel = "create table if not exists user_model(id integer primary key autoincrement ,username text,password text)"
cursor.execute(create_tabel)

connection.close()