from marshmallow import fields, Schema
from . import db
from .ArticleModel import ArticleSchema


class WriterModel(db.Model):

    # table name
    __tablename__ = 'writer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    articles = db.relationship('ArticleModel', backref='writer', lazy=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.age = data.get('age')
        self.email = data.get('email')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_writers():
        return WriterModel.query.all()

    @staticmethod
    def get_one_writer(id):
        return WriterModel.query.get(id)

    @staticmethod
    def get_writer_by_email(email):
        return WriterModel.query.filter_by(email=email).first()

    def __repr(self):
        return '<id {}>'.format(self.id)


class WriterSchema(Schema):

  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  age = fields.Int(required=True)
  email = fields.Email(required=True)
  articles = fields.Nested(ArticleSchema, many=True)