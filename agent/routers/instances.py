
import docker
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

client = docker.from_env()
router = APIRouter()



class Instance(BaseModel):
    template_id: str
    instance_id: str
    user_owner: str

@router.get("/instances/", tags=["instances"])
async def get_instances():
    return []

@router.post("/instances/{instance_id}/start", tags=["instances"])
async def spawn_instance(instance: Instance, instance_id: str):
    container_name = f"code-server-{instance_id}"
    try:
        existing = client.containers.get(container_name)
        if existing.status == "running":
            return {"status": "already_running", "name": container_name}
        existing.remove(force=True)
    except docker.errors.NotFound:
        pass

    try:
        container = client.containers.run(
            "codercom/code-server:latest",
            name=container_name,
            detach=True,
            auto_remove=True,
            environment={
                "PASSWORD": "Saturna",
            },
            volumes={
                f"{instance_id}": {
                    "bind": "/home/coder/project",
                    "mode": "rw",
                }
            }
        )
        return {"status": "started", "name": container_name, "id": container.id}

    except docker.errors.APIError as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.delete("/instances/{instance_id}", tags=["instances"])
# async def delete_instance(instance_id):
#     try:
#             existing = client.containers.get(container_name)
#             if existing.status == "running":
#                 return {"status": "already_running", "name": container_name}
#             existing.remove(force=True)
#         except docker.errors.NotFound:
#             pass
