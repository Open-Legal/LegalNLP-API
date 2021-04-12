from typing import Optional
from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uvicorn
import nltk
import types
import lexnlp.extract.en.definitions
import lexnlp.extract.en.durations
import lexnlp.extract.en.regulations
import lexnlp.extract.en.conditions
import lexnlp.extract.en.constraints
import lexnlp.extract.en.acts
import lexnlp.extract.en.dates
import lexnlp.extract.en.trademarks
import lexnlp.extract.en.percents
import lexnlp.extract.en.money
import lexnlp.extract.en.entities.nltk_maxent
import lexnlp.extract.en.entities.nltk_re

class Request(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Working"}

@app.post("/act")
def Act(item: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.acts.get_act_list(item.text)))

@app.post("/amount")
def Amount(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.amounts.get_amounts(item.text,True))))

@app.post("/constraint")
def Constraint(item: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.acts.get_act_list(item.text)))

@app.post("/company")
def Company(item: Request):
    return JSONResponse(content=jsonable_encoder((list(lexnlp.extract.en.entities.nltk_re.get_entities.nltk_re.get_companies(item.text)))))

@app.post("/date")
def Date(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.dates.get_dates(item.text))))

@app.post("/definition")
def Definition(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.definitions.get_definitions(item.text,True,True))))

@app.post("/duration")
def Duration(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.durations.get_durations(item.text))))

@app.post("/money")
def Money(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.money.get_money(item.text,True,4))))

@app.post("/regulation")
def Regulation(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.regulations.get_regulations(item.text,True,True))))

@app.post("/trademark")
def Regulation(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.trademarks.get_trademarks(item.text))))

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Open Legal - Legal NLP API",
        version="0.0.1",
        description="OpenAPI Schema for Legal NLP API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)