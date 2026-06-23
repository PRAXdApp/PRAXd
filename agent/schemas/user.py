from pydantic import BaseModel

from schemas.permissions import Permission


class User(BaseModel):
    firstname: str
    lastname: str
    image: bytes
    email: str
    modules: list
    roles: list
    permissions: list[Permission]

    def merge_permissions_with_roles(self):
        merged = set(self.permissions)
        for role in self.roles:
            merged.update()
