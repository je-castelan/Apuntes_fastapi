'''
uvicorn 02_paths:my_app --reload
'''

from fastapi import FastAPI

my_app = FastAPI()

# Also /docs and /redoc are ready


@my_app.get('/blog/')
def list_blogs():
    return {
        'data': 'All blogs list'
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
def get_blog(id: int):
    return {
        'data': {
            'blog': id,
            'comments': 'LOTS LOTS LOTS'
        }
    }