# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 16:19:47 2025

@author: formation
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Country(BaseModel):
    id: int = None
    name: str
    capital: str
    area: int
    
countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]
    
def _find_next_id():
    return max(country.id for country in countries) + 1

@app.get("/countries")
async def get_countries():
    return countries

@app.post("/countries", status_code=201)
async def add_country(country: Country):
    country.id = _find_next_id()
    countries.append(country)
    return country