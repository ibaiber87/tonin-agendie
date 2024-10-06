from datetime import datetime
from flask import Flask, render_template, jsonify, request
import requests
import os
import requests
from bs4 import BeautifulSoup
from scraping import scrap

app = Flask(__name__)


#VARIABLES*******************************************************
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://jqqiawmirueuvcxpdgvf.supabase.co") 
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpxcWlhd21pcnVldXZjeHBkZ3ZmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjQyNTUwNDQsImV4cCI6MjAzOTgzMTA0NH0.zmLSdua3EWJ9hhm8AlJugzLJahVmAOwi00bJdn8g2wY") 
data_json = []



#FUNCIONES BBDD**************************************************
def leer_BD():
    today = datetime.today().strftime('%Y-%m-%d')  # Obtener la fecha de hoy en formato 'YYYY-MM-DD'
    
    # Añadir el filtro para oculto<>'si' junto con las otras condiciones
    url = f"{SUPABASE_URL}/rest/v1/tbl_evento?fecha=gte.{today}&visible=eq.true&order=fecha.asc,provincia.asc"


    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        datos = response.json()
        return datos
    else:
        print(f"Error al obtener los datos: {response.status_code} - {response.text}")
        return []

def insertar(data):
    # Insertar en la tabla tbl_evento
    url_eventos = f"{SUPABASE_URL}/rest/v1/tbl_evento"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    # Realizar la inserción de cada evento en la tabla tbl_evento
    for evento in data:
        response = requests.post(url_eventos, headers=headers, json=evento)
        if response.status_code != 201:
            print(f"Error al insertar el evento: {response.status_code} - {response.text}")

    # Insertar el timestamp actual en la tabla tbl_timestamp
    url_timestamp = f"{SUPABASE_URL}/rest/v1/tbl_timestamp"
    timestamp_data = {
        "timestamp": datetime.now().isoformat()
    }
    response = requests.post(url_timestamp, headers=headers, json=timestamp_data)
    if response.status_code == 201:
        print("Timestamp insertado correctamente.")
    else:
        print(f"Error al insertar el timestamp: {response.status_code} - {response.text}")

    return True

def ocultar(ids):
    url = f"{SUPABASE_URL}/rest/v1/tbl_evento"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    for id in ids:
        # Construir la URL para actualizar un registro específico por su ID
        url_update = f"{url}?id=eq.{id}"
        
        # Datos a actualizar
        data = {
            "visible": False
        }
        
        # Realizar la solicitud PATCH para actualizar el campo oculto
        response = requests.patch(url_update, headers=headers, json=data)
        
        if response.status_code == 204:
            print(f"ID {id} actualizado correctamente.")
        else:
            print(f"Error al actualizar el ID {id}: {response.status_code} - {response.text}")

def eliminar():
    url = f"{SUPABASE_URL}/rest/v1/tbl_evento?id=gt.0"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    # Realiza la solicitud DELETE para eliminar todos los registros
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        return {"status": "success", "message": "Todos los registros han sido eliminados"}
    else:
        return {"status": "error", "message": f"Error al eliminar los registros: {response.status_code} - {response.text}"}
    

#RUTAS***********************************************************
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actualizar')
def actualizar():    
    data_json = []  # Reinicia el JSON cada vez que se actualiza
    print("Actualizando...")
    # Llama a las funciones de scraping para agregar datos
    data_json=scrap()

    # Llama a la función insertar con los datos obtenidos
    insertar(data_json)
    
    # Retorna un mensaje de éxito (o cualquier otra respuesta JSON si prefieres)
    return jsonify({"status": "success"})

@app.route('/descargar')
def descargar():
    # Llama a la función leer_BD para obtener los datos
    datos = leer_BD()    
    # Devuelve los datos como JSON    
    return jsonify(datos)

@app.route('/ocultar', methods=['POST'])
def ocultar_ruta():
    ids = request.json.get('ids', [])
    ocultar(ids)
    return jsonify({"status": "success", "ocultados": ids})

@app.route('/eliminar_todo', methods=['DELETE'])
def eliminar_todo():
    resultado = eliminar()  # Llama a la función eliminar y almacena el resultado
    return jsonify(resultado)  # Devuelve el resultado como respuesta JSON


#MAIN************************************************************
if __name__ == '__main__':
    app.run(debug=True)
