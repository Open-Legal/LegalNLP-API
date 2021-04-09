from typing import Optional
from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Request(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Working"}

@app.post("/act")
def read_item(req: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.acts.get_act_list(req.text)))

@app.post("/amount")
def read_item(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.amounts.get_amounts(text,True))))

@app.post("/constraint")
def read_item(req: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.acts.get_act_list(req.text)))