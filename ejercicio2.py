from dotenv import load_dotenv
import os
import requests
from deep_translator import GoogleTranslator

def traducir_descripcion(descripcion_en):
    try:
        traduccion = GoogleTranslator(source='en', target='es').translate(descripcion_en)
        return traduccion
    except Exception as e:
        print(f"Error en la traducción: {e}")
        return descripcion_en

def kelvin_to_celsius(grados_en_k):
    return grados_en_k - 273.15

load_dotenv()
api_key = os.getenv("API_KEY")


nombre_ciudad = input('Inserta el nombre de una ciudad: ')


url_openweathermap = f"https://api.openweathermap.org/data/2.5/weather?q={nombre_ciudad}&appid={api_key}"

try:
    
    response_get = requests.get(url_openweathermap)
    if response_get.status_code == 200:
        print('¡La solicitud a la API ha sido exitosa!')
        json_extraido = response_get.json()
        temperatura_actual_en_kelvin = json_extraido['main']['temp']
        temperatura_actual_en_celsius = kelvin_to_celsius(temperatura_actual_en_kelvin)
        descripcion_clima_en_ingles = json_extraido['weather'][0]['description']
        descripcion_clima_espanol = traducir_descripcion(descripcion_clima_en_ingles)
        print(f'El clima en {nombre_ciudad} es: {descripcion_clima_espanol}.')
        print(f'La temperatura actual en {nombre_ciudad} es de {round(temperatura_actual_en_celsius, 2)} grados Celsius.')
        
    else:
        print("¡Error! La solicitud a la API NO ha sido exitosa.")   

except requests.exceptions.HTTPError as e:
    print(f'Error HTTP: {e}')