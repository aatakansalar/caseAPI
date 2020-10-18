from pydantic import BaseModel
from typing import List, Dict


CONSTANTS = {
    "statusResponse": {"status": "ModelAPI is up and running!"},
    "argumentExample": {"body": "Bu harika bir filmdi."},
    "argumentsExample": {"argList": [{"body": "Bu güzel bir filmdi."}, {"body": "Bu kitabı hiç beğenmedim."}]},
}


class Argument(BaseModel):
    body: str


class Arguments(BaseModel):
    argList: List[Argument]


class ArgumentResponse(BaseModel):
    body: str
    evaluation: Dict


class ArgumentsResponse(BaseModel):
    evaluations: List
