from flask_restful import Api, Resource

from App.models import Goods

api = Api()

def init_api(app):
    api.init_app(app=app)



class MarketGoodsResource(Resource):
    def get(self):
        goods = Goods.query.all()

        return {'msg': 'ok'}

api.add_resource(MarketGoodsResource,'/market/')