import sqlite3
from src.db import db

class UserModel(db.Model):
    __tabelname__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self,username,password):
    #    self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()
        #
        # query = "select * from users where username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()
        #
        # query = "select * from users where id=?"
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user
