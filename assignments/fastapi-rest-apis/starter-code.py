from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST Assignment")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


items: dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API"}


@app.get("/items")
def list_items():
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": item}


@app.post("/items", status_code=201)
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items[item_id] = item
    return {"message": "Item created", "item_id": item_id, "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"message": "Item updated", "item_id": item_id, "item": item}
