from marshmallow import fields, Schema
import datetime
from . import db


class ArticleInBlogModel(db.Model):

    # table name
    __tablename__ = 'article_in_blog'

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.article_id = data.get('article_id')
        self.blog_id = data.get('blog_id')

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
    def get_all_articles_in_blog():
        return ArticleInBlogModel.query.all()

    @staticmethod
    def get_one_article_in_one_blog(blog_id):
        return ArticleInBlogModel.query.filter_by(blog_id=blog_id).all()

    @staticmethod
    def get_one_article_in_blog(id):
        return ArticleInBlogModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class ArticleInBlogSchema(Schema):

  id = fields.Int(dump_only=True)
  article_id = fields.Int(required=True)
  blog_id = fields.Int(required=True)