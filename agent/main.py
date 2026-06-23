import docker
from typing import Annotated, Literal, Union
from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel, Field, TypeAdapter, ValidationError
from .routers.instances import router as InstanceRouter
from .routers.websocket import ws as WebsocketHandler
app = FastAPI()
client = docker.from_env()

app.include_router(InstanceRouter)
