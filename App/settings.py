def get_db_uri(dbinfo):
    user = dbinfo.get('USER') or 'root'
    password = dbinfo.get('PASSWORD') or '123456'
    host = dbinfo.get('HOST') or '127.0.0.1'
    port = dbinfo.get('PORT') or '3306'
    name = dbinfo.get('NAME') or 'AXFpython1801'
    db = dbinfo.get('DB') or 'mysql'
    dirver = dbinfo.get('dirver') or 'pymysql'
    return "{}+{}://{}:{}@{}:{}/{}".format(db, dirver, user, password, host, port, name)


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'USEER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'AXFpython1801',
        'DB': 'mysql',
        'dirver': 'pymysql'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = False
    DATABASE = {
        'USEER': 'ROOT',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'HelloFlask',
        'DB': 'mysql',
        'dirver': 'pymysql'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StaggingConfig(Config):
    DEBUG = True
    DATABASE = {
        'USEER': 'ROOT',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'HelloFlask',
        'DB': 'mysql',
        'dirver': 'pymysql'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = True
    DATABASE = {
        'USEER': 'ROOT',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'HelloFlask',
        'DB': 'mysql',
        'dirver': 'pymysql'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


config = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'stagging': StaggingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}
