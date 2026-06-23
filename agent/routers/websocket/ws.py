import docker
from typing import Annotated, Literal, Union
from fastapi import APIRouter, HTTPException, WebSocket
from pydantic import BaseModel, Field, TypeAdapter, ValidationError


router = APIRouter(prefix="/ws/")


class InstancesMessage(BaseModel):
    scope: Literal["instances"]
    action: Literal["start", "stop", "restart", "logs"]

class AdminMessage(BaseModel):
    scope: Literal["admin"]
    action: Literal["list_user", "create_user", "delete_user"]

WebsocketMessage = Annotated[
    Union[InstancesMessage, AdminMessage],
    Field(discriminator="scope"),
]

adapter = TypeAdapter(WebsocketMessage)

@router.websocket("/admin")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        raw = await websocket.receive_json()
        try:
            data = adapter.validate_python(raw)
        except ValidationError:
            continue
        if data.scope == "instances":
            print("Le scope est instances")
        if data.scope == "admin":
            print("Le scope est admin")
        continue
