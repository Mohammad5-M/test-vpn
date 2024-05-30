from pyrog import main2

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def read_item():
    return Response(main2(),200)