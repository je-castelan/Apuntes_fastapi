'''
uvicorn 04_body_request:my_app --reload
'''
from typing import Optional
from fastapi import FastAPI


my_app = FastAPI()


# CHECK THIS
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@my_app.post('/blog/')
def create_blog(request: Blog):
    return {"result": f"Blog {request.title} created", "data": request}



@my_app.get('/blog/')
def list_blogs(
    limit: int = 10, published: bool = True, # mandatory query params
    name: Optional[str] = None # optional query params
): 
    message: str =  f'Blogs limited in {limit} and status as {published}.'
    if name:
        message += f' Also getting with name {name}'
    return {
        'data': message
    }


@my_app.get('/blog/unpublished/')
def unpublished():
    return {
        'data': 'All is death'
    }


@my_app.get('/blog/{id}/')
def get_blog(id: int): # very neccesary to specify typing   
    return {
        'data': {
            'blog': id,
            'name': f'Blog number {id}'
        }
    }


@my_app.get('/blog/{id}/comments')
def get_blog(
    id: int, # path
    limit: int = 10
):
    return {
        'data': {
            'blog': id,
            'comments': f'{limit} comments found'
        }
    }
