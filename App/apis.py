from flask import Blueprint


api = Blueprint('api', __name__)

def init_api(app):
    app.register_blueprint(blueprint=api)

# class Home