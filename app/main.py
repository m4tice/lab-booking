"""Main"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import unsplash, twoforms, accordion
from .library.helpers import openfile


# =========================================================
#### INITIALIZATION #######################################
# =========================================================

# app creation
app = FastAPI()

# router
app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)

# directories
TEMPLATE_DIRECTORY = "./templates"
STATIC_DIRECTORY = "./static"

templates = Jinja2Templates(directory=TEMPLATE_DIRECTORY)
app.mount("/static", StaticFiles(directory=STATIC_DIRECTORY), name="static")


# =========================================================
#### VIEWS CREATION #######################################
# =========================================================

# Example URL: http://127.0.0.1:8000/
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Home page
    """
    # data = {
    #     "page": "Home Page"
    # }

    data = openfile("home.md")

    return templates.TemplateResponse("page.html", {"request": request, "data": data})


# Example URL: http://127.0.0.1:8000/page/m4tice
@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    """
    Specific page
    """
    # data = {
    #     "page": page_name
    # }
    data = openfile(page_name + ".md")

    return templates.TemplateResponse("page.html", {"request": request, "data": data})


def main():
    """
    main function
    """
    # something here


if __name__ == "__main__":
    main()
