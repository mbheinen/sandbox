from typing import List

from pydantic import BaseModel

from nmm.models import Model

class GetModelByIDQuery(BaseModel):
    id: str

    def execute(self) -> Model:
        article = Model.get_by_id(self.id)

        return article

class ListModelsQuery(BaseModel):

    def execute(self) -> List[Model]:
        models = Model.list()

        return models
