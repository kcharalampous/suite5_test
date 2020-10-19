from flask import request, json, Response, Blueprint
from ..models.BlogModel import BlogModel, BlogSchema

blog_api = Blueprint('blog', __name__)
blog_schema = BlogSchema()


@blog_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data = blog_schema.load(req_data)

    blog = BlogModel(data)
    blog.save()

    return custom_response({'message': "Successfully created blog"}, 200)


@blog_api.route('/all', methods=['GET'])
def read_all():
    blogs = BlogModel.get_all_blogs()
    response = blog_schema.dump(blogs, many=True)
    return custom_response(response, 200)


@blog_api.route('/<int:blog_id>', methods=['PUT'])
def update(blog_id):
    req_data = request.get_json()
    data = blog_schema.load(req_data, partial=True)
    blog = BlogModel.get_one_blog(blog_id)
    blog.update(data)
    response = blog_schema.dump(blog)

    return custom_response(response, 200)


@blog_api.route('/<int:blog_id>', methods=['GET'])
def read_one(blog_id):
    blog = BlogModel.get_one_blog(blog_id)
    response = blog_schema.dump(blog)
    return custom_response(response, 200)


@blog_api.route('/<int:blog_id>', methods=['DELETE'])
def delete(blog_id):
    article = BlogModel.get_one_blog(blog_id)
    article.delete()
    return custom_response({"message": "Deleted blog successfully"}, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
