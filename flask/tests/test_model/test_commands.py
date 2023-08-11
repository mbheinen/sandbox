import pytest

from nmm.models import Model
from nmm.commands import CreateModelCommand, AlreadyExists


def test_create_model():
    """
    GIVEN CreateModelCommand with a valid properties name and slug
    WHEN the execute method is called
    THEN a new Model must exist in the database with the same attributes
    """
    cmd = CreateModelCommand(
        name='Texas Energy Transmission',
        slug='te-transmission'
    )

    model = cmd.execute()

    db_model = Model.get_by_id(model.id)

    assert db_model.id == model.id
    assert db_model.name == model.name
    assert db_model.slug == model.slug


def test_create_model_already_exists():
    """
    GIVEN CreateModelCommand with a slug of some model already in database
    WHEN the execute method is called
    THEN the AlreadyExists exception must be raised
    """

    Model(
        name='Texas Energy Transmission',
        slug='te-transmission',
    ).save()

    cmd = CreateModelCommand(
        name='Tampa Energy Transmission',
        slug='te-transmission'
    )

    with pytest.raises(AlreadyExists):
        cmd.execute()