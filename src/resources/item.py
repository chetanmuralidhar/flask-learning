import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import Flask,jsonify,request
from src.models.Item import ItemModel
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('store_id',
                        type=float,
                        required=True,
                        help="Every time needs a store id")
    #@jwt_required()
    def get(self, name):

        item = ItemModel.find_by_name(name)

        if item:
            return item.json()


        return {'message':'An item not found'},404




    def post(self, name):

        if ItemModel.find_by_name(name):
            return {'message': 'An item with name ' + name + 'already exists'}, 400

        data = Item.parser.parse_args()

        # data = request.get_json(force=False, silent=False, cache=True)
       # item = ItemModel(name,data['price'],data['store_id'])
        item = ItemModel(name,**data)
        try:
            item.save_to_db()                       #  item.insert()
        except:
            return {'message':'An error occured while inserting'},500

        return item.json(), 201

    def delete(self, name):

        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()
        # query = "delete from items where name=?"
        # cursor.execute(query, (name,))
        # connection.commit()
        # connection.close()
        return {'message': 'Items deleted'}

    def put(self, name):

        # data = request.get_json()
        # item = ItemModel.find_by_name(name)
        # updated_item = ItemModel( name,data['price'])
        # if item is None:
        #     updated_item.insert()
        # else:
        #     updated_item.update()
        data = request.get_json()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()
        #
        # query = "select * from items"
        # result = cursor.execute(query)
        #
        #
        # items=[]
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})

        return {'items':[item.json() for item in ItemModel.query.all()]},200
