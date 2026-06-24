from uuid import UUID, uuid4

from pydantic import BaseModel

from .permissions import Permission


class Role(BaseModel):
    name: str
    id: UUID
    permissions: list[Permission]


def mock_roles() -> list[Role]:
    return [
        Role(
            name = "root",
            id = uuid4(),
            permissions = [Permission.ROOT_ALL]
        )
    ]
