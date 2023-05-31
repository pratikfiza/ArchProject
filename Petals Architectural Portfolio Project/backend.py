from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dbcon import get_db_connector
from sqlalchemy import select

from fastapi import FastAPI, Request, File, UploadFile, Form, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from dbcon import get_db_connector, select, insert
from sqlalchemy import update
from pydantic import BaseModel
import uvicorn
from datetime import datetime, timedelta


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')







class insert_customer_msg(BaseModel):
    name: str
    email: str
    message:str
    phone:str
    subject:str

def insert_msg_data(name,email,msg,phone,subject):
    table, engine = get_db_connector('customer_messages')
    query = insert(table).values(name=name,email=email,msg=msg,phone=phone,subject=subject)
    engine.execute(query)

@app.post("/add_customer_msg")
def add_data(insert_data: insert_customer_msg):
    data = jsonable_encoder(insert_data)
    print(data)
    insert_msg_data(data['name'],data['email'],data['message'],data['phone'],data['subject'])
    return {'success': 'Article Inserted'}



@app.get('/about')
def load_home(request: Request):
   
    # data = get_all_photos()
    return templates.TemplateResponse('about.html',context={'request': request, })




@app.get('/project')
def load_home(request: Request):

    return templates.TemplateResponse('project.html',context={'request': request})


@app.get('/2d')
def load_home(request: Request):

    return templates.TemplateResponse('2d.html',context={'request': request})

@app.get('/interior')
def load_home(request: Request):

    return templates.TemplateResponse('design.html',context={'request': request})



@app.get('/3d')
def load_home(request: Request):

    return templates.TemplateResponse('3d.html',context={'request': request})





@app.get('/book')
def load_home(request: Request):

    return templates.TemplateResponse('book.html',context={'request': request})


@app.get('/contactus')
def load_home(request: Request):

    return templates.TemplateResponse('contact.html',context={'request': request})




@app.get("/admin")
def redirect_admin():
    try:
        response = RedirectResponse(url="http://localhost:8002/")
        return response
    except:
        raise HTTPException(status_code=500, detail="Internal server error")



@app.get('/')
def load_home(request: Request):

    return templates.TemplateResponse('index.html',context={'request': request})


if __name__ == "__main__":
    uvicorn.run('backend:app', host='localhost', port=8003, reload=True)