from fastapi import APIRouter


def build_placeholder_router(resource_name: str) -> APIRouter:
    router = APIRouter(tags=[resource_name])

    @router.post("/", summary=f"Create {resource_name}")
    def create_item(payload: dict):
        return {"resource": resource_name, "action": "create", "payload": payload}

    @router.get("/", summary=f"List {resource_name}")
    def list_items():
        return {"resource": resource_name, "action": "list", "items": []}

    @router.get("/{item_id}", summary=f"Get {resource_name} detail")
    def detail_item(item_id: int):
        return {"resource": resource_name, "action": "detail", "id": item_id}

    @router.put("/{item_id}", summary=f"Update {resource_name}")
    def update_item(item_id: int, payload: dict):
        return {"resource": resource_name, "action": "update", "id": item_id, "payload": payload}

    return router
