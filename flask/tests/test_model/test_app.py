import json
import pathlib
import os

import requests
import pytest
from jsonschema import validate, RefResolver

from nmm.app import app
from nmm.models import Model

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def validate_payload(payload, schema_name):
    """
    Validate payload with selected schema
    """
    schemas_dir = str(
        f'{pathlib.Path(__file__).parent.absolute()}{os.path.sep}schemas'
    )
    schema = json.loads(pathlib.Path(f'{schemas_dir}{os.path.sep}{schema_name}').read_text())
    validate(
        payload,
        schema,
        resolver=RefResolver(
            'file://' + str(pathlib.Path(f'{schemas_dir}{os.path.sep}{schema_name}').absolute()),
            schema  # it's used to resolve file: inside schemas correctly
        )
    )


def test_create_model(client):
    """
    GIVEN request data for new model
    WHEN endpoint /models/ is called
    THEN it should return Model in json format matching schema
    """
    data = {
        'name': 'Texas Energy Transmission',
        'slug': 'te-transmission'
    }
    response = client.post(
        '/articles/',
        data=json.dumps(
            data
        ),
        content_type='application/json',
    )

    validate_payload(response.json, 'Model.json')


def test_get_model(client):
    """
    GIVEN ID of model stored in the database
    WHEN endpoint /model/<id-of-model>/ is called
    THEN it should return Model in json format matching schema
    """
    model = Model(
        name='Texas Energy Transmission',
        slug='te-transmission'
    ).save()
    response = client.get(
        f'/models/{model.id}/',
        content_type='application/json',
    )

    validate_payload(response.json, 'Model.json')


def test_list_models(client):
    """
    GIVEN models stored in the database
    WHEN endpoint /models/ is called
    THEN it should return list of Model in json format matching schema
    """
    Model(
        name='Texas Energy Transmission',
        slug='te-transmission'
    ).save()
    response = client.get(
        '/models/',
        content_type='application/json',
    )

    validate_payload(response.json, 'ModelList.json')

@pytest.mark.parametrize(
    'data',
    [
        {
            'name': 'Texas Energy Transmission'
        },
        {
            'name': 'Texas Energy Distribution',
            'slug': 'te%#trubtion',
        },
        {
            'name': 'Futures Energy ISO',
            'slug': 'fe  -iso'
        }
    ]
)
def test_create_model_bad_request(client, data):
    """
    GIVEN request data with invalid values or missing attributes
    WHEN endpoint /models/ is called
    THEN it should return status 400 and JSON body
    """
    response = client.post(
        '/models/',
        data=json.dumps(
            data
        ),
        content_type='application/json',
    )

    assert response.status_code == 400
    assert response.json is not None


@pytest.mark.e2e
def test_create_list_get(client):
    requests.post(
        'http://localhost:5000/models/',
        json={
            'name': 'Texas Energy Transmission',
            'slug': 'te-transmission'
        }
    )
    response = requests.get(
        'http://localhost:5000/models/',
    )

    models = response.json()

    response = requests.get(
        f'http://localhost:5000/models/{models[0]["id"]}/',
    )

    assert response.status_code == 200