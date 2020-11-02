import sqlite3
from flask_restful import Resource
from flask import Flask,jsonify,request
from src.models.user import UserModel
class UserRegister(Resource):
    def post(self):
        data = request.get_json()

        if UserModel.find_by_username(data['username']):
            return {"message":"Username already exists"},400

        user = UserModel(**data)
        user.save_to_db()
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()
        #
        # query = "insert into users values (NULL,?,?)"
        # cursor.execute(query,(data['username'],data['password']))
        #
        # connection.commit()
        # connection.close()

        return {"message":"user created successfully"},201