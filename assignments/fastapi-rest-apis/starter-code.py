from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST Assignment")


class Item(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0)


items = {
    1: {"name": "Notebook", "description": "14-inch laptop", "price": 4200.0},
    2: {"name": "Mouse", "description": "Wireless mouse", "price": 120.0},
}


@app.get("/")
def read_root():
    return {"message": "API online"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    next_id = max(items.keys(), default=0) + 1
    items[next_id] = item.model_dump()
    return {"id": next_id, **items[next_id]}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    items[item_id] = item.model_dump()
    return {"id": item_id, **items[item_id]}
