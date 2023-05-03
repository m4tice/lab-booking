"""Main"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# app creation
app = FastAPI()


# Example URL: http://127.0.0.1:8000/
@app.get("/")
async def home():
    """
    Home page
    """
    data = {
        "text": "Hello World"
    }

    return {"data": data}


# Example URL: http://127.0.0.1:8000/page/m4tice
@app.get("/page/{page_name}")
async def page(page_name: str):
    """
    Specific page
    """
    data = {
        "page": page_name
    }

    return {"data": data}


def main():
    """
    main function
    """
    # something here


if __name__ == "__main__":
    main()
