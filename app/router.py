from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Boilerplate",
    description="A boilerplate project for FastAPI.",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {
        "message": "Hello, FastAPI!"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id
    }
