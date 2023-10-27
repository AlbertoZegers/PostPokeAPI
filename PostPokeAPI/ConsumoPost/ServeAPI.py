from fastapi import FastAPI, Query
import requests

url = "https://pokeapi.co/api/v2/pokemon/"

app = FastAPI()
@app.post('/post')
@app.get('/post')
async def serve_post(post: str = Query(..., description="Nombre del Pokémon")):
    respuesta = requests.get(url+post)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return {f"Error en la solicitud. Código de estado: {respuesta.status_code}"}
    
@app.get('/')
async def serve_get():
    return {"Indicaciones": "Use la ruta http://127.0.0.1:8000/post?post=pikachu"}

# respuesta=requests.get(url+"pikachu")
# print(respuesta.json())