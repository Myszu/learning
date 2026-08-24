from typing import Optional
from fastapi import APIRouter, Request, Header, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import datetime, timezone, timedelta

from db.config import get_db
from db import models, crud
from modules.logger import Logger

router = APIRouter() #miejsce na endpointy administratora
templates: Jinja2Templates = Jinja2Templates(directory='templates') #renderowanie HTML  z floderu templates

LOGGER = Logger(__name__, 'admin').create()

@router.get('/', response_class=HTMLResponse)
async def admin_get(
    request: Request,
    db: Session = Depends(get_db)
):
    admins = crud.Admins(db).get_all_admins()
    admins[1].name = "test_dwa"
    db.commit()
    
    context = {
        'request': request,
        'admins': admins
    }
    
    try: 
        return templates.TemplateResponse(request, name='indx.html', context=context) # Returns admin panel page
    except:
        LOGGER.exception('Admin Page not found or corrupted.')