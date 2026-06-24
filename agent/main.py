import docker
from fastapi import FastAPI
from .routers.instances import router as InstanceRouter
from .schemas.user import user1
app = FastAPI()
client = docker.from_env()

app.include_router(InstanceRouter)


@app.get("/uinfo")
def user_info():
    return user1.permissions
