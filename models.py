from pydantic import BaseModel
from typing import List


class Column(BaseModel):
    name: str
    datatype: str


class Table(BaseModel):
    name: str
    columns: List[Column]


class ForeignKey(BaseModel):
    table: str
    column: str
    references_table: str
    references_column: str


class DatabaseSchema(BaseModel):
    tables: List[Table]