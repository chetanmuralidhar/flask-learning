
from src.db import db
class StoreModel(db.Model):
    __tabelname__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship("ItemModel", back_populates="items")

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name


    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}

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
        #return ItemModel.query.filter_by(name=name).first()
        return cls.query.filter_by(name=name).first()

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