from pydantic import BaseModel

class City(BaseModel):
    id: int
    name: str
    district: str
    population: int

class Country(BaseModel):
    code: str
    name: str
    continent: str
    region: str
    capital: City