from marshmallow import fields, Schema
from . import db


class BlogModel(db.Model):

    # table name
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.title = data.get('title')

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
    def get_all_blogs():
        return BlogModel.query.all()

    @staticmethod
    def get_one_blog(id):
        return BlogModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class BlogSchema(Schema):
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)