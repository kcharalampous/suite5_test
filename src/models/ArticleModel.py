from marshmallow import fields, Schema
import datetime
from . import db


class ArticleModel(db.Model):

    # table name
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    excerpt = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('writer.id'), nullable=False)
    image = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.title = data.get('title')
        self.excerpt = data.get('excerpt')
        self.text = data.get('text')
        self.writer_id = data.get('writer_id')
        self.image = data.get('image')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_articles():
        return ArticleModel.query.all()

    @staticmethod
    def get_one_article(id):
        return ArticleModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class ArticleSchema(Schema):
  """
  User Schema
  """
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)
  excerpt = fields.Str(required=True)
  text = fields.Str(required=True)
  writer_id = fields.Int(required=True)
  image = fields.Str(required=False)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)