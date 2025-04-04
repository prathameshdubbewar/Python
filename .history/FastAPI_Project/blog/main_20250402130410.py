from fastapi import FastAPI
from pydantic import BaseModel
import models
import database  # Make sure this is correct

app = FastAPI()


models.Base.metadata.create_all(database.engine)

class Blog(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create(request: Blog):
    return request
