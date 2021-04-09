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
def Act(req: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.acts.get_act_list(req.text)))

@app.post("/amount")
def Amount(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.amounts.get_amounts(text,True))))

@app.post("/constraint")
def Constraint(req: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.acts.get_act_list(req.text)))

@app.post("/company")
def Company(req: Request):
    return JSONResponse(content=jsonable_encoder((list(lexnlp.extract.en.entities.nltk_re.get_entities.nltk_re.get_companies(text)))))

@app.post("/date")
def Date(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.dates.get_dates(text))))

@app.post("/definition")
def Definition(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.definitions.get_definitions(text,True,True))))

@app.post("/duration")
def Duration(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.durations.get_durations(text))))

@app.post("/money")
def Money(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.money.get_money(text,True,4))))

@app.post("/regulation")
def Regulation(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.regulations.get_regulations(text,True,True))))

@app.post("/trademark")
def Regulation(req: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.trademarks.get_trademarks(text))))