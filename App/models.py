from App.ext import db


class Goods(db.Model):
    productid = db.Column(db.Integer(16))
    productimg = db.Column(db.String(200))
    productname = db.Column(db.String(100))
    productlongname = db.Column(db.String(200))
    isxf = db.Column(db.Integer,default=1)
    pmdesc = db.Column(db.String(100))
    specifics = db.Column(db.String(100))
    price = db.Column(db.Float,default=0)
    marketprice = db.Column(db.String(16))
    categoryid = db.Column(db.String(16))
    childcid = db.Column(db.String(16))
    childcidname = db.Column(db.String(100))
    dealerid = db.Column(db.String(16))
    storenums = db.Column(db.Integerg,default=1)
    productnum = db.Column(db.Integer,default=1)

    class Meta:
        db_table = "axf_goods"