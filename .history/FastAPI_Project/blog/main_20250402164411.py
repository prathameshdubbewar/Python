from fastapi import FastAPI
from pydantic import BaseModel
from . import models, database

app = FastAPI()

models.Base.metadata.create_all(database.engine)

class Blog(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create(request: Blog):
    return request

