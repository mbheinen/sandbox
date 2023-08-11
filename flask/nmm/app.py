from flask import Flask, jsonify, request

from nmm.commands import CreateModelCommand
from nmm.queries import GetModelByIDQuery, ListModelsQuery
from pydantic import ValidationError

app = Flask(__name__)

@app.errorhandler(ValidationError)
def handle_validation_exception(error):
    response = jsonify(error.errors())
    response.status_code = 400
    return response

@app.route('/models/', methods=['POST'])
def create_article():
    cmd = CreateModelCommand(
        **request.json
    )
    return jsonify(cmd.execute().dict())


@app.route('/models/<model_id>/', methods=['GET'])
def get_model(model_id):
    query = GetModelByIDQuery(
        id=model_id
    )
    return jsonify(query.execute().dict())


@app.route('/models/', methods=['GET'])
def list_models():
    query = ListModelsQuery()
    records = [record.dict() for record in query.execute()]
    return jsonify(records)


if __name__ == '__main__':
    app.run()