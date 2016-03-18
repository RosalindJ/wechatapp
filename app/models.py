# import datetime
# from flask.ext.mongoengine import MongoEngine
#
# db = MongoEngine()
#
#
# class Shop(db.Document):
#     sid = db.StringField(max_length=40)
#     href = db.URLField()
#
#
# class Product(db.Document):
#     pid = db.StringField(max_length=40)
#     href = db.URLField()
#     keywords = db.StringField()
#     shop = db.ReferenceField(Shop)
#
#
# class Detail(db.Document):
#     product = db.ReferenceField(Product)
#     rate = db.StringField()
#     detail = db.StringField()
#     price = db.StringField()
#     deal = db.StringField()
#
#
# class Presell(db.Document):
#     username = db.StringField()
#     phone = db.StringField()
#     created_time = db.DateTimeField(default=datetime.datetime.now)
