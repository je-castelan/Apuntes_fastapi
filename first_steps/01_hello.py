"""
uvicorn 01_hello:app --reload
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        "data": {
            "message": "Hello Ary"
        }
    }

@app.get('/about/')
def about():
    return {
        "data": {
            "message": "This is my first Fast API"
        }
    }