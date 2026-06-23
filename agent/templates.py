from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Literal

class Template(BaseModel):
    name: str
    id: UUID
    baseimage: Literal["debian", "ubuntu", "nixos", "codercom/code-server:4.125.0-39"]
    packages: list[str]
    tags: list[str]



registred_templates: list[Template] = [
    Template(
        name = "codeserver",
        id = uuid4(),
        baseimage = "codercom/code-server:4.125.0-39",
        packages = [],
        tags = []
    )
]
