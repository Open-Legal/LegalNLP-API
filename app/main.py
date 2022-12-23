from typing import Optional, List
from fastapi import FastAPI, Depends
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uvicorn
import nltk
import types
import spacy
import lexnlp.extract.en.definitions
import lexnlp.extract.en.durations
import lexnlp.extract.en.regulations
import lexnlp.extract.en.conditions
import lexnlp.extract.en.constraints
from lexnlp.extract.en.entities.company_detector import CompanyDetector
from lexnlp.extract.en.entities.nltk_maxent import get_company_annotations
import lexnlp.extract.en.acts
import lexnlp.extract.en.dates
import lexnlp.extract.en.trademarks
import lexnlp.extract.en.percents
import lexnlp.extract.en.money
import lexnlp.extract.en.amounts
import lexnlp.extract.en.entities.nltk_maxent
import lexnlp.extract.en.entities.nltk_re
import lexnlp.extract.en.geoentities
from models.Leg import Leg
from models.NamedEntity import NamedEntity
from models.Abrv import Abrv
from models.FCAContent import FCAContent
import regex
from collections import OrderedDict

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
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.amounts.get_amounts(item.text))))


@app.post("/constraint")
def Constraint(item: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.constraints.get_constraints(item.text)))


@app.post("/company")
def Company(item: Request):
    return JSONResponse(content=jsonable_encoder(
        (list(get_company_annotations(item.text)))))

@app.post("/date")
def Date(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.dates.get_dates(item.text))))

@app.post("/definition")
def Definition(item: Request):
    return JSONResponse(
        content=jsonable_encoder(list(lexnlp.extract.en.definitions.get_definitions(item.text, True, True))))

@app.post("/distances")
def Distance(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.distances.get_distances(item.text))))

@app.post("/duration")
def Duration(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.durations.get_durations(item.text))))


@app.post("/fca")
def FCA(item: Request):

    baseUrl = "https://www.handbook.fca.org.uk/handbook/"

    matches = regex.findall("[A-Z]+\s(?>Sch\s)?(?>Ann\s)?(?>TP\s)?\d+[A-Z]?(?>\.\d+)*-?\s?[A-Z]?", item.text)

    # Strip whitespace from matches
    stripped = [s.strip() for s in matches]

    # Get only unique values
    unique = list(dict.fromkeys(stripped))

    items = []  # type: List[FCAContent]

    for value in unique:

        section = regex.findall("[A-Z]+\s(?>Sch\s)?(?>Ann\s)?(?>TP\s)?", value)[0].split()
        sub = regex.findall("\d+[A-Z]?(?>\.\d+)*-?\s?[A-Z]?", value)[0].split('.')

        url = baseUrl + section[0] + "/"

        if len(section) == 2:
            url = url + section[1] + "/"

        if len(sub) != 0:
            url = url + sub[0] + "/" + sub[0] + ".html"
        
        items.append(FCAContent(value, findall(item.text, value), url))

    return JSONResponse(content=jsonable_encoder(items))


@app.post("/money")
def Money(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.money.get_money(item.text, True, 4))))

@app.post("/regulation")
def Regulation(item: Request):
    return JSONResponse(
        content=jsonable_encoder(list(lexnlp.extract.en.regulations.get_regulations(item.text, True, True))))

@app.post("/sentences")
def Sentences(item: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.nlp.en.segments.sentences.get_sentence_list(item.text)))

@app.post("/trademark")
def Regulation(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.trademarks.get_trademarks(item.text))))

def findall(text, sub):
    """Return all indices at which substring occurs in text"""
    return [
        index
        for index in range(len(text) - len(sub) + 1)
        if text[index:].startswith(sub)
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)