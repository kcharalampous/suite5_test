import os


class FlaskConfig(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost/db'
