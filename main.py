from fastapi import FastAPI, status;
from pydantic import BaseModel;
from typing import List;
from decouple import config;
from supabase import create_client,Client;
import random

url=config("SUPABASE_URL")
key=config("SUPABASE_KEY")


app=FastAPI()
supabase : Client =create_client(url,key)
class Tea(BaseModel):
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

@app.get("/tea/{id}")
def get_tea(id:int):
    tea_data=supabase.table("Teas").select("*").eq("id",id).execute()
    return tea_data


@app.post("/teas/", status_code=status.HTTP_201_CREATED)
def add_tea(tea:Tea):
    id=random.randint(0,100)
    created_tea=supabase.table("Teas").insert({
        "id":id,
        "name":tea.name,
        "origin":tea.origin
    }).execute()
    return created_tea


@app.delete("/teas/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_tea(id:int):
   supabase.table("Teas").delete().eq("id",id).execute()
   return {"msg":"Deleted"}