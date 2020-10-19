from flask import request, json, Response, Blueprint, g
from ..models.WriterModel import WriterModel, WriterSchema

writer_api = Blueprint('writer', __name__)
writer_schema = WriterSchema()


@writer_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data = writer_schema.load(req_data)

    writer_in_db = WriterModel.get_writer_by_email(data.get('email'))
    if writer_in_db:
        message = {'error': 'Writer already exist, please supply another email address'}
        return custom_response(message, 400)

    writer = WriterModel(data)
    writer.save()

    return custom_response({'mgs': "Successfully created writer"}, 200)


@writer_api.route('/all', methods=['GET'])
def read_all():
    writers = WriterModel.get_all_writers()
    response = writer_schema.dump(writers, many=True)
    return custom_response(response, 200)


@writer_api.route('/<int:writer_id>', methods=['PUT'])
def update(writer_id):
    req_data = request.get_json()
    data = writer_schema.load(req_data, partial=True)
    writer = WriterModel.get_one_writer(writer_id)
    writer.update(data)
    response = writer_schema.dump(writer)

    return custom_response(response, 200)


@writer_api.route('/<int:writer_id>', methods=['GET'])
def read_one(writer_id):
    writer = WriterModel.get_one_writer(writer_id)
    response = writer_schema.dump(writer)
    return custom_response(response, 200)


@writer_api.route('/<int:writer_id>', methods=['DELETE'])
def delete(writer_id):
    writer = WriterModel.get_one_writer(writer_id)
    writer.delete()
    return custom_response({"message": "Deleted writer successfully"}, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
