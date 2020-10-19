from flask import request, json, Response, Blueprint, g
from ..models.ArticleModel import ArticleModel, ArticleSchema

article_api = Blueprint('article', __name__)
article_schema = ArticleSchema()


@article_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data = article_schema.load(req_data)

    artcle = ArticleModel(data)
    artcle.save()

    return custom_response({'message': "Successfully created article"}, 200)


@article_api.route('/all', methods=['GET'])
def read_all():
    articles = ArticleModel.get_all_articles()
    response = article_schema.dump(articles, many=True)
    return custom_response(response, 200)


@article_api.route('/<int:article_id>', methods=['PUT'])
def update(article_id):
    req_data = request.get_json()
    data = article_schema.load(req_data, partial=True)
    article = ArticleModel.get_one_article(article_id)
    article.update(data)
    response = article_schema.dump(article)

    return custom_response(response, 200)


@article_api.route('/<int:article_id>', methods=['GET'])
def read_one(article_id):
    article = ArticleModel.get_one_article(article_id)
    response = article_schema.dump(article)
    return custom_response(response, 200)


@article_api.route('/<int:article_id>', methods=['DELETE'])
def delete(article_id):
    article = ArticleModel.get_one_article(article_id)
    article.delete()
    return custom_response({"message": "Deleted article successfully"}, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
