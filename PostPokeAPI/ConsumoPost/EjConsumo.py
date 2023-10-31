import requests
import os

api_url = "http://127.0.0.1:8000/post?post="  

pokemon = str(input("Ingrese el nombre del Pokémon:"))  

response = requests.post(api_url+pokemon)

if response.status_code == 200:
    pokemon_data = response.json()
    print("Datos del Pokémon:", pokemon_data)
else:
    print("Error al obtener datos del Pokémon.")
os.system("pause")