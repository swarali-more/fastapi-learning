from fastapi import FastAPI
from practice.day3.schemas import Item

app = FastAPI()

fake_db = {}

@app.post("/items")
def get_items(item: Item):
    fake_db[item.name] = item
    return item