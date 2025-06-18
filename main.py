from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncpg
from telebot import get_photo_tg

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.secret_key = 'MyV3ryS3cr3tK!3y_L0ngAndStr0ng'


# Подключение бд для всех страниц

@app.on_event("startup")
async def startup():
    app.state.pool = await asyncpg.create_pool(
        database="Admin",
        host="localhost", 
        user="postgres",
        password="root", 
        port="8887"
    )


# Home Page

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    
   async with app.state.pool.acquire() as conn:
       rows = await conn.fetch("select * from admin")
    
   #photo_tg = await get_photo_tg() "photo_tg": photo_tg

   return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

