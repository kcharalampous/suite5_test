from flask import Flask

from .models import db, ArticleModel, BlogModel, WriterModel, ArticleInBlogModel
from .config import FlaskConfig
from .views.WriterView import writer_api as writer_blueprint # add this line
from .views.ArticleView import article_api as article_blueprint # add this line
from .views.ArticleInBlogView import article_in_blog_api as article_ib_blog_blueprint # add this line
from .views.BlogView import blog_api as blog_blueprint # add this line


def create_app():
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    db.init_app(app)

    app.register_blueprint(writer_blueprint, url_prefix='/api/v1/writer')
    app.register_blueprint(article_blueprint, url_prefix='/api/v1/article')
    app.register_blueprint(article_ib_blog_blueprint, url_prefix='/api/v1/article_in_blog')
    app.register_blueprint(blog_blueprint, url_prefix='/api/v1/blog')

    return app
