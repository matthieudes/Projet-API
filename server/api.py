from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"welcome to fastapi"}


@app.get("/items")
def get_items():
    return[
        {"id":1, "description": "Item 1"},
        {"id":2, "description": "Item 1"},
        {"id":3, "description": "Item 1"},
    ]