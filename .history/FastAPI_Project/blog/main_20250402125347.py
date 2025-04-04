from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas,models 
from database import engine
app = FastAPI()


models.Base.metadata.create_all(engine)

class Blog(BaseModel):
    title: str
    body : str
@app.post('/blog')
def create(request: Blog):
    return request

