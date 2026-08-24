# GLOBAL IMPORTS
import uvicorn, logging #uruchamia serwer / logi
from typing import Optional #zmienna moze miec okreslony typ albo None
from contextlib import asynccontextmanager #generator asynchroniczny
from fastapi import FastAPI, Request, Form, Depends #tworzenie serwera, żądanie użytkownika, dane z formularzy, DB
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates #generowanie html
from fastapi.staticfiles import StaticFiles #css, js, img
from sqlalchemy.orm import Session #polaczenie z baza

# LOGGING FORMATTER
logging.basicConfig(format=f'%(asctime)s | %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO, filename='./logs/server.log', force=True)

# LOCAL IMPORTS
from modules import config as cfg
from db import models, crud
from db.config import engine, get_db
from routers import admin #endpointy administratora

models.Base.metadata.create_all(bind=engine) #podczas uruchamiania aplikacji laduje modele, laczy sie z baza upewnia sie ze wymagane tabele istnieja jak nie to je tworzy

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    logging.info('Server startup...')
    
    yield
    
    #SHUTDOWN
    logging.info('Server shutdown...')
    
app: FastAPI = FastAPI( #glowny obiekt aplikacji
    lifespan=lifespan,
    docs_url=None if not cfg.DEBUGGING else "/docs", #chowanie tych dwoch stronek konfiguracyjnych jak nie jestesmy w tyrybie debuggowania (cfg)
    redoc_url=None if not cfg.DEBUGGING else "/redoc"
)

# TEMPLATES AND STATIC FILES HTML, CSS, img, js
templates: Jinja2Templates = Jinja2Templates(directory='templates') #obiekt odpowiedzialny za szablony html
app.mount('/css', StaticFiles(directory='static/css'), name='css')
app.mount('/img', StaticFiles(directory='static/img'), name='img')
app.mount('/js', StaticFiles(directory='static/js'), name='js')

# ROUTERS dodanie do glownej aplikacji wszystkie endpointy admin, poprzedzanie ich adresow '/admin' i tagi
app.include_router(admin.router, prefix='/admin', tags=['admin', 'panel'])

# GET, POST
@app.get('/', response_class=HTMLResponse) #dekorator FastAPI ('/' - strona glowna, ta funkcja bedzie zwracala html)
async def index_get(
    request: Request, #FastAPI automatycznie przekazuje obniakt aktualnego żądania HTTP
    db: Session = Depends(get_db) #to mowi ze do sesji potrzeba bazy danych, pobiera ja za pomoca get_db() i przekazuje do zmiennej db
):
    admins = crud.Admins(db).get_all_admins() #pobiera liste administratorow z bazy
    admins[1].name = "test_dwa" #podmienia nazwe 2 adm 
    db.commit() #zapisuje zmiany w bazie
    
    context = { #slownik ktory zostanie przekazany do szablonu HTML
        'request': request, 
        'admins': admins
    }
    
    try: #probujemy wygenerowac strone
        return templates.TemplateResponse(request, name='inex.html', context=context) #literowka 
    except: #wypluwa logi jak cos pojdzie nie tak
        logging.exception('Index page not found or corrupted.')

@app.get('/sub', response_class=HTMLResponse) #drugi endpoint
async def subpage_get(
    request: Request
):
    context = {
        'request': request
    }
    
    
    return templates.TemplateResponse(request, name='index2.html', context=context) 

if __name__ == "__main__": #sprawdza czy odpalasz z glownego pliku
    if cfg.DEBUGGING: #sprawdza czy odpalamy w trybie zwyklym czy developerskim
        uvicorn.run(app='main:app', host=cfg.DEBUGGING_SOCKET, port=cfg.DEBUGGING_PORT, reload=True) # HTTP -> 80, HTTPS -> 443
    else: # PROD MODE  
        uvicorn.run(app='main:app', host='0.0.0.0', port=80, reload=True) # HTTP -> 80, HTTPS -> 443