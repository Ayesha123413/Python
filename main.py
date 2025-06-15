from fastapi import FastAPI;
from pydantic import BaseModel;
from typing import List;
from decouple import config;
from supabase import create_client,Client;

url=config("SUPABASE_URL")
key=config("SUPABASE_KEY")


app=FastAPI()
supabase : Client =create_client(url,key)
class Tea(BaseModel):
    id:int
    name:str
    origin:str

teas:List[Tea]=[]

@app.get("/")
def read_root():
    return {"message": "welcome to tea house"}

@app.get("/teas")
def  get_teas():
    Teas_data=supabase.table("Teas").select("*").execute()
    return Teas_data

@app.get("/tea${tea_id}")
def get_tea(id:int):
    tea_data=supabase.table("Teas").select("*").eq("id",id).execute()
    return tea_data


@app.post("/teas")
def add_tea(tea:Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int ,updated_tea:Tea):
    for index,tea in enumerate(teas):
        if tea.id==tea_id:
            teas[index]=updated_tea
            return updated_tea
    return {"error":"Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int):
    for index,tea in enumerate(teas):
        if tea.id==tea_id:
            deleted=teas.pop(index)
            return deleted
    return {"error":"tea not found"}