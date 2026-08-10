# GLOBAL IMPORTS
import uvicorn, logging
from typing import Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

# LOGGING FORMATTER
logging.basicConfig(format=f'%(asctime)s | %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO, filename='./logs/server.log', force=True)

# LOCAL IMPORTS
from modules import config as cfg
from db import models, crud
from db.config import engine, get_db
from routers import admin

models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    logging.info('Server startup...')
    
    yield
    
    #SHUTDOWN
    logging.info('Server shutdown...')
    
app: FastAPI = FastAPI(
    lifespan=lifespan,
    docs_url=None if not cfg.DEBUGGING else "/docs",
    redoc_url=None if not cfg.DEBUGGING else "/redoc"
)

# TEMPLATES AND STATIC FILES
templates: Jinja2Templates = Jinja2Templates(directory='templates')
app.mount('/css', StaticFiles(directory='static/css'), name='css')
app.mount('/img', StaticFiles(directory='static/img'), name='img')
app.mount('/js', StaticFiles(directory='static/js'), name='js')

# ROUTERS
app.include_router(admin.router, prefix='/admin', tags=['admin', 'panel'])

# GET, POST
@app.get('/', response_class=HTMLResponse)
async def index_get(
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
        return templates.TemplateResponse(request, name='inex.html', context=context)
    except:
        logging.exception('Index page not found or corrupted.')

@app.get('/sub', response_class=HTMLResponse)
async def subpage_get(
    request: Request
):
    context = {
        'request': request
    }
    
    
    return templates.TemplateResponse(request, name='index2.html', context=context)

if __name__ == "__main__":
    if cfg.DEBUGGING:
        uvicorn.run(app='main:app', host=cfg.DEBUGGING_SOCKET, port=cfg.DEBUGGING_PORT, reload=True) # HTTP -> 80, HTTPS -> 443
    else: # PROD MODE  
        uvicorn.run(app='main:app', host='0.0.0.0', port=80, reload=True) # HTTP -> 80, HTTPS -> 443