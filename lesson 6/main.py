import uvicorn
from typing import Optional
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from db import models, crud
from db.config import engine, get_db

models.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI()
templates: Jinja2Templates = Jinja2Templates(directory='templates')
app.mount('/css', StaticFiles(directory='static/css'), name='css')
app.mount('/img', StaticFiles(directory='static/img'), name='img')
app.mount('/js', StaticFiles(directory='static/js'), name='js')

# GET, POST
@app.get('/', response_class=HTMLResponse)
def index_get(
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
    
    return templates.TemplateResponse(request, name='index.html', context=context)

@app.get('/sub', response_class=HTMLResponse)
def subpage_get(
    request: Request
):
    context = {
        'request': request
    }
    
    return templates.TemplateResponse(request, name='index2.html', context=context)

@app.post('/sub', response_class=HTMLResponse)
def subpage_post(
    request: Request,
    name: Optional[str] = Form(None)
):
    context = {
        'request': request,
        'name': name
    }
    
    return templates.TemplateResponse(request, name='index2.html', context=context)

if __name__ == "__main__":
    uvicorn.run(app='main:app', host='0.0.0.0', port=80, reload=True)