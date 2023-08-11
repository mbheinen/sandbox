import os
import sqlite3
import uuid
from typing import List, Optional

import datetime
from pydantic import BaseModel, Field, validator


class NotFound(Exception):
    pass


class Model(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    slug: str
    updated: Optional[datetime.datetime]

    @validator('slug')
    def slug_validate(cls, v):
        chars = set('!@#$%^&*()_./\ ')
        if any((c in chars) for c in v):
            raise ValueError('must not contain any of "!@#$%^&*()_./\ "')
        return v.title()

    @classmethod
    def get_by_id(cls, model_id: str):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM models WHERE id=?", (model_id,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        model = cls(**record)  # Row can be unpacked as dict
        con.close()

        return model

    @classmethod
    def get_by_slug(cls, slug: str):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM models WHERE slug = ?", (slug,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        model = cls(**record)  # Row can be unpacked as dict
        con.close()

        return model

    @classmethod
    def list(cls) -> List['Model']:
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM models")

        records = cur.fetchall()
        models = [cls(**record) for record in records]
        con.close()

        return models

    def save(self) -> 'Model':
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO models (id,name,slug,updated) VALUES(?, ?, ?, ?)",
                (self.id, self.name, self.slug, datetime.datetime.now(datetime.timezone.utc))
            )
            con.commit()

        return self

    @classmethod
    def create_table(cls, database_name='database.db'):
        conn = sqlite3.connect(database_name)

        conn.execute(
            'CREATE TABLE IF NOT EXISTS models (id TEXT, name TEXT, slug TEXT, updated TIMESTAMP)'
        )
        conn.close()