import requests
from bs4 import BeautifulSoup
from datetime import datetime
from funciones import *

def scrap():
    data_json = []
    #data_json.extend(scrap_musika_zuzenean())
    data_json.extend(scrap_prosineck())
    
    return data_json

def scrap_musika_zuzenean():
    url = "https://musikazuzenean.eus/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error al acceder a la página: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    data_json = []

    current_date = None

    for element in soup.find_all(['div']):
        if 'events__date' in element.get('class', []):
            day = element.find("div", class_="events__date-calendar-day").get_text(strip=True)
            month = element.find("div", class_="events__date-calendar-month").get_text(strip=True)
            month = obtener_mes(month)
            year = obtener_anio(day, month)
            current_date = f"{year}/{month}/{day}"

        if 'event__card' in element.get('class', []):
            artistas = lugar_info = poblacion = provincia = lugar = link =imagen_url= None

            try:
                artistas = element.find("div", class_="event__bands").get_text(strip=True)
            except AttributeError:
                pass

            try:
                lugar_info = element.find("div", class_="event__where").get_text(strip=True)
                poblacion, provincia = lugar_info.split('(')
                provincia = provincia.replace(')', '').strip()
            except AttributeError:
                pass

            try:
                lugar = element.find("div", class_="event__info").get_text(strip=True)
            except AttributeError:
                pass

            try:
                link = element.find("a", href=True)["href"]
            except AttributeError:
                pass
                        
            try:
                imagen_element = element.find("a", class_="event__image lazyload")
                if imagen_element:
                    imagen_url = imagen_element['data-bg-image']
                    imagen_url=imagen_url[4:-1]
            except AttributeError:
                pass
            
            hora, precio, detalles = None, None, None
            if link:
                hora, precio, detalles = scrap_musika_zuzenean_details(link)            
                
            evento = {
                "fecha": current_date,
                "hora": hora,
                "lugar": lugar,
                "provincia": provincia,
                "poblacion": poblacion,
                "tipo": "Musikie",
                "artistas": artistas,
                "precio": precio,
                "detalles": detalles,
                "link": link,
                "imagen":imagen_url,
                "web": "Musikazuzenean"
            }

            data_json.append(evento)

    return data_json

def scrap_musika_zuzenean_details(event_url):
    response = requests.get(event_url)
    if response.status_code != 200:
        print(f"Error al acceder a la página del evento: {response.status_code}")
        return None, None, None

    soup = BeautifulSoup(response.content, "html.parser")

    try:
        hora = None
        hora = soup.find("div", class_="single-event__date-calendar-time").get_text(strip=True)
    except AttributeError:
        hora = None

    try:
        precio = None
        precio = soup.find("div", class_="single-event__price").get_text(strip=True)
    except AttributeError:
        precio = None

    try:
        detalles = None
        detalles = soup.find("div", class_="single-event__description").get_text(strip=True)
    except AttributeError:
        detalles = None

    return hora, precio, detalles

def scrap_prosineck():
    url = "https://www.prosineck.es/1/Agenda.html"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error al acceder a la página: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    data_json = []
    current_date = None

    for element in soup.select("ul#mynews > li"):
        # Si encontramos un elemento con clase 'fecha', actualizamos current_date
        fecha_element = element.find("p", class_="fecha")
        if fecha_element:
            current_date = fecha_element.get_text(strip=True)
            # Quitar el día de la semana
            partes_fecha = current_date.split(' ', 1)[1]  # Esto quita el día de la semana
            dia, mes_nombre = partes_fecha.split(' de ')

            # Obtener el número del mes
            mes = obtener_mes(mes_nombre)

            # Calcular el año
            anio = obtener_anio(dia, mes)

            # Construir la fecha en formato dd/mm/yyyy
            fecha_formateada = f"{anio}/{mes}/{dia}"            

        # Ahora extraemos los datos de cada concierto bajo la fecha actual
        for concierto in element.find_all("div", class_="concierto"):
            # Inicializar todas las variables a None
            hora = None
            precio = None
            lugar = None
            poblacion = None
            provincia = None
            artistas = None
            link = None
            detalles = None
            imagen_url=None

            # Extraer la hora y precio
            hora_precio_element = concierto.find("p", class_="hora_precio")
            if hora_precio_element:
                hora_text = hora_precio_element.contents[0].strip()  # Obtén el primer contenido de hora_precio_element
                hora = hora_text if ":" in hora_text else None  # Verifica si es una hora válida

                precio_span = hora_precio_element.find("span", class_="negrita")
                if precio_span:
                    precio = precio_span.get_text(strip=True)  # Extrae el precio del span

            # Extraer lugar y ubicación
            lugar_info = concierto.find("span", class_="lugar")
            if lugar_info:
                lugar = lugar_info.get_text(strip=True)
                location_text = lugar_info.find_next_sibling(text=True)
                if location_text:
                    location_text = location_text.strip()
                    if "(" in location_text:
                        poblacion, detalles = location_text.split("(", 1)
                        poblacion = poblacion.strip()[2:]  # Eliminar los primeros dos caracteres y espacios
                        detalles = detalles.rstrip(")").strip()
                    else:
                        poblacion = location_text.strip()[2:]  # Eliminar los primeros dos caracteres y espacios
                        detalles = None

            provincia = obtener_provincia(poblacion)
            
            # Extraer artistas
            artistas_list = []
            for grupo in concierto.find_all("div", class_="grupos"):
                for artista in grupo.find_all("a"):
                    artistas_list.append(artista.get_text(strip=True))
            artistas = ", ".join(artistas_list)

            # Extraer la URL de la imagen
            cartel_div = concierto.find("div", class_="cartel")
            if cartel_div:
                enlace_imagen = cartel_div.find("a", class_="colorbox")
                if enlace_imagen:
                    imagen_url = enlace_imagen['href'] 


            # Crear el diccionario del evento
            evento = {
                "fecha": fecha_formateada,
                "hora": hora,
                "lugar": lugar,
                "provincia": provincia,
                "poblacion": poblacion,
                "tipo": "Musikie",
                "artistas": artistas,
                "precio": precio,
                "detalles": detalles,
                "link": url,
                "imagen":imagen_url,
                "web": "Prosineck"
            }

            # Añadir el evento al JSON global
            data_json.append(evento)  

    return data_json
