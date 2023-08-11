from pydantic import BaseModel

from nmm.models import Model, NotFound


class AlreadyExists(Exception):
    pass


class CreateModelCommand(BaseModel):
    name: str
    slug: str

    def execute(self) -> Model:
        try:
            Model.get_by_slug(self.slug)
            raise AlreadyExists
        except NotFound:
            pass

        article = Model(
            name=self.name,
            slug=self.slug
        ).save()

        return article