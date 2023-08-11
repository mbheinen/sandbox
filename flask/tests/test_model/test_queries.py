from nmm.models import Model
from nmm.queries import ListModelsQuery, GetModelByIDQuery


def test_list_models():
    """
    GIVEN 2 models stored in the database
    WHEN the execute method is called
    THEN it should return 2 models
    """
    Model(
        name='Texas Energy Transmission',
        slug='te-transmission',
    ).save()
    Model(
        name='Texas Energy Distribution',
        slug='te-distribution',
    ).save()

    query = ListModelsQuery()

    assert len(query.execute()) == 2

def test_get_model_by_id():
    """
    GIVEN ID of model stored in the database
    WHEN the execute method is called on GetModelByIDQuery with id set
    THEN it should return the model with the same id
    """
    model = Model(
        name='Texas Energy Transmission',
        slug='te-transmission',
    ).save()

    query = GetModelByIDQuery(
        id=model.id
    )

    assert query.execute().id == model.id