from flask import request, json, Response, Blueprint, g
from ..models.ArticleInBlogModel import ArticleInBlogModel, ArticleInBlogSchema

article_in_blog_api = Blueprint('article_in_blog', __name__)
article_in_blog_schema = ArticleInBlogSchema()


@article_in_blog_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data = article_in_blog_schema.load(req_data)

    artcle = ArticleInBlogModel(data)
    artcle.save()

    return custom_response({'message': "Successfully created article in blog"}, 200)


@article_in_blog_api.route('/all', methods=['GET'])
def read_all():
    blog_id = request.args.get('blog_id')
    if blog_id is not None:
        articles = ArticleInBlogModel.get_one_article_in_one_blog(blog_id)
    else:
        articles = ArticleInBlogModel.get_all_articles_in_blog()
    response = article_in_blog_schema.dump(articles, many=True)
    return custom_response(response, 200)


@article_in_blog_api.route('/<int:article_in_blog_id>', methods=['PUT'])
def update(article_in_blog_id):
    req_data = request.get_json()
    data = article_in_blog_schema.load(req_data, partial=True)
    article_in_blog = ArticleInBlogModel.get_one_article_in_blog(article_in_blog_id)
    article_in_blog.update(data)
    response = article_in_blog_schema.dump(article_in_blog)

    return custom_response(response, 200)


@article_in_blog_api.route('/<int:article_in_blog_id>', methods=['GET'])
def read_one(article_in_blog_id):
    article = ArticleInBlogModel.get_one_article_in_blog(article_in_blog_id)
    response = article_in_blog_schema.dump(article)
    return custom_response(response, 200)

@article_in_blog_api.route('/', methods=['GET'])
def read_all_from_blog(article_in_blog_id):
    blog_id = request.args.get('blog_id')
    articles = ArticleInBlogModel.get_one_article_in_one_blog(blog_id)
    response = article_in_blog_schema.dump(articles, many=True)
    return custom_response(response, 200)


@article_in_blog_api.route('/<int:article_in_blog_id>', methods=['DELETE'])
def delete(article_in_blog_id):
    article = ArticleInBlogModel.get_one_article_in_blog(article_in_blog_id)
    article.delete()
    return custom_response({"message": "Deleted article in blog successfully"}, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
