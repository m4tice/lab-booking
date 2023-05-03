"""Unsplash"""

from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


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
    return templates.TemplateResponse("unsplash.html", {"request": request})
