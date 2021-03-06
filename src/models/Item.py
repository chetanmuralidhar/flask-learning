
from src.db import db
class ItemModel(db.Model):
    __tabelname__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        # self.store_id = store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_by_name(cls,name):
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()
        #
        # query = "select * from items where name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        #
        # if row:
        #     return cls(*row)  # cls(row[0],row[1])
        return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self):   # def insert(self):
        # connection = sqlite3.connect('mydata.db')
        # cursor = connection.cursor()
        # query = "insert into items values(?,?)"
        # cursor.execute(query, (self.name, self.price,))
        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()




    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # def update(self):
    #     connection = sqlite3.connect('mydata.db')
    #     cursor = connection.cursor()
    #     query = "update items set price=? where name=?"
    #     cursor.execute(query, (self.price, self.name,))
    #     connection.commit()
    #     connection.close()