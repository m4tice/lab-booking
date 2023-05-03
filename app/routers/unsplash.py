"""Unsplash"""

import os

from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..library.helpers import print_master

from dotenv import load_dotenv
load_dotenv()


# templates
TEMPLATE_DIRECTORY = "./templates"
STATIC_DIRECTORY = "./static"

# template creation
templates = Jinja2Templates(directory=TEMPLATE_DIRECTORY)

# router creation
router = APIRouter()

@router.get("/unsplash", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    """
    unplash home
    """
    key = os.getenv("unsplash_key")
    print_master(key)

    return templates.TemplateResponse("unsplash.html", {"request": request})
