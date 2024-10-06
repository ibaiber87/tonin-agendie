from datetime import datetime

#FUNCIONES AUXILIARES********************************************
def obtener_mes(mes):
    # Diccionario que mapea los nombres de los meses en euskera a su valor numérico
    meses = {
        # Euskera - 3 letras
        'Urt': "01",    
        'Ots': "02",    
        'Mar': "03",
        'Api': "04",
        'Mai': "05",
        'Eka': "06",
        'Uzt': "07",
        'Abu': "08",
        'Ira': "09",
        'Urr': "10",
        'Aza': "11",
        'Abe': "12",

        # Euskera - completo
        'Urtarrila': "01",    
        'Otsaila': "02",    
        'Martxoa': "03",
        'Apirila': "04",
        'Maiatza': "05",
        'Ekaina': "06",
        'Uztaila': "07",
        'Abuztua': "08",
        'Iraila': "09",
        'Urria': "10",
        'Azaroa': "11",
        'Abendua': "12",

        # Castellano - 3 letras
        'Ene': "01",
        'Feb': "02",
        'Mar': "03",
        'Abr': "04",
        'May': "05",
        'Jun': "06",
        'Jul': "07",
        'Ago': "08",
        'Sep': "09",
        'Oct': "10",
        'Nov': "11",
        'Dic': "12",

        # Castellano - completo
        'Enero': "01",
        'Febrero': "02",
        'Marzo': "03",
        'Abril': "04",
        'Mayo': "05",
        'Junio': "06",
        'Julio': "07",
        'Agosto': "08",
        'Septiembre': "09",
        'Octubre': "10",
        'Noviembre': "11",
        'Diciembre': "12",
    }

    return meses.get(mes, "Mes no válido")

def obtener_anio(dia, mes):
    # Obtener la fecha actual y solo considerar la parte de la fecha (sin la hora)
    hoy = datetime.now().date()

    # Crear la fecha proporcionada con el año actual y comparar solo la fecha (sin la hora)
    fecha_proporcionada = datetime(datetime.now().year, int(mes), int(dia)).date()
    
    # Si la fecha proporcionada es igual o mayor a hoy, el año es el actual
    if fecha_proporcionada >= hoy:
        return hoy.year
    else:
        # Si la fecha proporcionada ya pasó este año, el año es el siguiente
        return hoy.year + 1

def obtener_provincia(poblacion):
    mapa_provincias = {
        # Bizkaia
        "Abadiño": "Bizkaia",
        "Abanto y Ciérvana": "Bizkaia",
        "Ajangiz": "Bizkaia",
        "Alonsotegi": "Bizkaia",
        "Amorebieta-Etxano": "Bizkaia",
        "Amoroto": "Bizkaia",
        "Arakaldo": "Bizkaia",
        "Arantzazu": "Bizkaia",
        "Areatza": "Bizkaia",
        "Arrankudiaga": "Bizkaia",
        "Arratzu": "Bizkaia",
        "Arrieta": "Bizkaia",
        "Arrigorriaga": "Bizkaia",
        "Artea": "Bizkaia",
        "Artzentales": "Bizkaia",
        "Atxondo": "Bizkaia",
        "Aulesti": "Bizkaia",
        "Bakio": "Bizkaia",
        "Balmaseda": "Bizkaia",
        "Barakaldo": "Bizkaia",
        "Barrika": "Bizkaia",
        "Basauri": "Bizkaia",
        "Bedia": "Bizkaia",
        "Berango": "Bizkaia",
        "Bermeo": "Bizkaia",
        "Berriatua": "Bizkaia",
        "Berriz": "Bizkaia",
        "Bilbao": "Bizkaia",
        "Busturia": "Bizkaia",
        "Derio": "Bizkaia",
        "Dima": "Bizkaia",
        "Durango": "Bizkaia",
        "Ea": "Bizkaia",
        "Elantxobe": "Bizkaia",
        "Elorrio": "Bizkaia",
        "Erandio": "Bizkaia",
        "Ereño": "Bizkaia",
        "Ermua": "Bizkaia",
        "Errigoiti": "Bizkaia",
        "Etxebarri": "Bizkaia",
        "Etxebarria": "Bizkaia",
        "Forua": "Bizkaia",
        "Fruiz": "Bizkaia",
        "Galdakao": "Bizkaia",
        "Galdames": "Bizkaia",
        "Gamiz-Fika": "Bizkaia",
        "Garai": "Bizkaia",
        "Gatika": "Bizkaia",
        "Gautegiz Arteaga": "Bizkaia",
        "Gernika-Lumo": "Bizkaia",
        "Getxo": "Bizkaia",
        "Gizaburuaga": "Bizkaia",
        "Gordexola": "Bizkaia",
        "Gorliz": "Bizkaia",
        "Güeñes": "Bizkaia",
        "Ibarrangelu": "Bizkaia",
        "Igorre": "Bizkaia",
        "Ispaster": "Bizkaia",
        "Iurreta": "Bizkaia",
        "Izurtza": "Bizkaia",
        "Karrantza Harana/Valle de Carranza": "Bizkaia",
        "Karrantza Harana": "Bizkaia",
        "Valle de Carranza": "Bizkaia",
        "Kortezubi": "Bizkaia",
        "Lanestosa": "Bizkaia",
        "Larrabetzu": "Bizkaia",
        "Laukiz": "Bizkaia",
        "Leioa": "Bizkaia",
        "Lekeitio": "Bizkaia",
        "Lemoa": "Bizkaia",
        "Lemoiz": "Bizkaia",
        "Lezama": "Bizkaia",
        "Loiu": "Bizkaia",
        "Llodio":"Bizkaia",
        "Laudio":"Bizkaia",
        "Mallabia": "Bizkaia",
        "Mañaria": "Bizkaia",
        "Markina-Xemein": "Bizkaia",
        "Markina": "Bizkaia",
        "Xemein": "Bizkaia",
        "Maruri-Jatabe": "Bizkaia",
        "Maruri": "Bizkaia",
        "Jatabe": "Bizkaia",
        "Mendata": "Bizkaia",
        "Mendexa": "Bizkaia",
        "Meñaka": "Bizkaia",
        "Morga": "Bizkaia",
        "Mundaka": "Bizkaia",
        "Mungia": "Bizkaia",
        "Munitibar-Arbatzegi Gerrikaitz": "Bizkaia",
        "Munitibar": "Bizkaia",
        "Arbatzegi Gerrikaitz": "Bizkaia",
        "Murueta": "Bizkaia",
        "Muskiz": "Bizkaia",
        "Muxika": "Bizkaia",
        "Nabarniz": "Bizkaia",
        "Ondarroa": "Bizkaia",
        "Orozko": "Bizkaia",
        "Ortuella": "Bizkaia",
        "Otxandio": "Bizkaia",
        "Plentzia": "Bizkaia",
        "Portugalete": "Bizkaia",
        "Santurtzi": "Bizkaia",
        "Sestao": "Bizkaia",
        "Sondika": "Bizkaia",
        "Sopelana": "Bizkaia",
        "Sopuerta": "Bizkaia",
        "Sukarrieta": "Bizkaia",
        "Trucios-Turtzioz": "Bizkaia",
        "Trucios": "Bizkaia",
        "Turtzioz": "Bizkaia",
        "Ubide": "Bizkaia",
        "Ugao-Miraballes": "Bizkaia",
        "Ugao": "Bizkaia",
        "Miraballes": "Bizkaia",
        "Urduliz": "Bizkaia",
        "Urduña/Orduña": "Bizkaia",
        "Urduña": "Bizkaia",
        "Orduña": "Bizkaia",
        "Valle de Trápaga-Trapagaran": "Bizkaia",
        "Valle de Trápaga": "Bizkaia",
        "Trapagaran": "Bizkaia",
        "Zaldibar": "Bizkaia",
        "Zalla": "Bizkaia",
        "Zamudio": "Bizkaia",
        "Zaratamo": "Bizkaia",
        "Zeanuri": "Bizkaia",
        "Zeberio": "Bizkaia",
        "Zierbena": "Bizkaia",
        "Zornotza": "Bizkaia",

        # Gipuzkoa
        "Abaltzisketa": "Gipuzkoa",
        "Aduna": "Gipuzkoa",
        "Aia": "Gipuzkoa",
        "Aizarnazabal": "Gipuzkoa",
        "Albiztur": "Gipuzkoa",
        "Alegia": "Gipuzkoa",
        "Alkiza": "Gipuzkoa",
        "Altzaga": "Gipuzkoa",
        "Altzo": "Gipuzkoa",
        "Amezketa": "Gipuzkoa",
        "Andoain": "Gipuzkoa",
        "Anoeta": "Gipuzkoa",
        "Antzuola": "Gipuzkoa",
        "Arama": "Gipuzkoa",
        "Aretxabaleta": "Gipuzkoa",
        "Arrasate/Mondragón": "Gipuzkoa",
        "Arrasate": "Gipuzkoa",
        "Mondragón": "Gipuzkoa",
        "Asteasu": "Gipuzkoa",
        "Astigarraga": "Gipuzkoa",
        "Ataun": "Gipuzkoa",
        "Azkoitia": "Gipuzkoa",
        "Azpeitia": "Gipuzkoa",
        "Baliarrain": "Gipuzkoa",
        "Beasain": "Gipuzkoa",
        "Beizama": "Gipuzkoa",
        "Belauntza": "Gipuzkoa",
        "Berastegi": "Gipuzkoa",
        "Bergara": "Gipuzkoa",
        "Berrobi": "Gipuzkoa",
        "Bidania-Goiatz": "Gipuzkoa",
        "Bidania": "Gipuzkoa",
        "Goiatz": "Gipuzkoa",
        "Deba": "Gipuzkoa",
        "Donostia-San Sebastián": "Gipuzkoa",
        "Donostia": "Gipuzkoa",
        "San Sebastián": "Gipuzkoa",
        "Eibar": "Gipuzkoa",
        "Elduain": "Gipuzkoa",
        "Elgeta": "Gipuzkoa",
        "Elgoibar": "Gipuzkoa",
        "Errenteria": "Gipuzkoa",
        "Errezil": "Gipuzkoa",
        "Eskoriatza": "Gipuzkoa",
        "Ezkio-Itsaso": "Gipuzkoa",
        "Ezkio": "Gipuzkoa",
        "Itsaso": "Gipuzkoa",
        "Gabiria": "Gipuzkoa",
        "Gaintza": "Gipuzkoa",
        "Gaztelu": "Gipuzkoa",
        "Getaria": "Gipuzkoa",
        "Hernani": "Gipuzkoa",
        "Hernialde": "Gipuzkoa",
        "Hondarribia": "Gipuzkoa",
        "Ibarra": "Gipuzkoa",
        "Idiazabal": "Gipuzkoa",
        "Ikaztegieta": "Gipuzkoa",
        "Irun": "Gipuzkoa",
        "Irura": "Gipuzkoa",
        "Itsasondo": "Gipuzkoa",
        "Larraul": "Gipuzkoa",
        "Lasarte-Oria": "Gipuzkoa",
        "Lasarte": "Gipuzkoa",
        "Oria": "Gipuzkoa",
        "Lazkao": "Gipuzkoa",
        "Leaburu": "Gipuzkoa",
        "Legazpi": "Gipuzkoa",
        "Legorreta": "Gipuzkoa",
        "Leintz-Gatzaga": "Gipuzkoa",
        "Lezo": "Gipuzkoa",
        "Lizartza": "Gipuzkoa",
        "Mendaro": "Gipuzkoa",
        "Mutiloa": "Gipuzkoa",
        "Mutriku": "Gipuzkoa",
        "Oiartzun": "Gipuzkoa",
        "Olaberria": "Gipuzkoa",
        "Oñati": "Gipuzkoa",
        "Ordizia": "Gipuzkoa",
        "Orendain": "Gipuzkoa",
        "Orexa": "Gipuzkoa",
        "Orio": "Gipuzkoa",
        "Ormaiztegi": "Gipuzkoa",
        "Pasaia": "Gipuzkoa",
        "Segura": "Gipuzkoa",
        "Soraluze/Placencia de las Armas": "Gipuzkoa",
        "Soraluze": "Gipuzkoa",
        "Placencia de las Armas": "Gipuzkoa",
        "Tolosa": "Gipuzkoa",
        "Urnieta": "Gipuzkoa",
        "Urretxu": "Gipuzkoa",
        "Usurbil": "Gipuzkoa",
        "Villabona": "Gipuzkoa",
        "Zaldibia": "Gipuzkoa",
        "Zarautz": "Gipuzkoa",
        "Zegama": "Gipuzkoa",
        "Zerain": "Gipuzkoa",
        "Zestoa": "Gipuzkoa",
        "Zizurkil": "Gipuzkoa",
        "Zumaia": "Gipuzkoa",
        "Zumarraga": "Gipuzkoa",

        # Álava
        "Alegría-Dulantzi": "Álava",
        "Alegría": "Álava",
        "Dulantzi": "Álava",
        "Amurrio": "Álava",
        "Añana": "Álava",
        "Aramaio": "Álava",
        "Armiñón": "Álava",
        "Arraia-Maeztu": "Álava",
        "Arraia": "Álava",
        "Maeztu": "Álava",
        "Arratzua-Ubarrundia": "Álava",
        "Arratzua": "Álava",
        "Ubarrundia": "Álava",
        "Artziniega": "Álava",
        "Asparrena": "Álava",
        "Ayala/Aiara": "Álava",
        "Ayala": "Álava",
        "Aiara": "Álava",
        "Baños de Ebro/Mañueta": "Álava",
        "Baños de Ebro": "Álava",
        "Mañueta": "Álava",
        "Barrundia": "Álava",
        "Berantevilla": "Álava",
        "Bernedo": "Álava",
        "Campezo/Kanpezu": "Álava",
        "Campezo": "Álava",
        "Kanpezu": "Álava",
        "Elburgo/Burgelu": "Álava",
        "Elburgo": "Álava",
        "Burgelu": "Álava",
        "Elciego": "Álava",
        "Elvillar/Bilar": "Álava",
        "Elvillar": "Álava",
        "Bilar": "Álava",
        "Harana/Valle de Arana": "Álava",
        "Harana": "Álava",
        "Valle de Arana": "Álava",
        "Iruña Oka/Iruña de Oca": "Álava",
        "Iruña Oka": "Álava",
        "Iruña de Oca": "Álava",
        "Iruraiz-Gauna": "Álava",
        "Kripan": "Álava",
        "Kuartango": "Álava",
        "Labastida/Bastida": "Álava",
        "Labastida": "Álava",
        "Bastida": "Álava",
        "Lagrán": "Álava",
        "Laguardia": "Álava",
        "Lanciego/Lantziego": "Álava",
        "Lanciego": "Álava",
        "Lantziego": "Álava",
        "Lantarón": "Álava",
        "Lapuebla de Labarca": "Álava",
        "Laudio/Llodio": "Álava",
        "Laudio": "Álava",
        "Llodio": "Álava",
        "Legutio": "Álava",
        "Leza": "Álava",
        "Moreda de Álava": "Álava",
        "Navaridas": "Álava",
        "Okondo": "Álava",
        "Oyón-Oion": "Álava",
        "Oyón": "Álava",
        "Oion": "Álava",
        "Peñacerrada-Urizaharra": "Álava",
        "Peñacerrada": "Álava",
        "Urizaharra": "Álava",
        "Ribera Alta": "Álava",
        "Ribera Baja/Erribera Beitia": "Álava",
        "Ribera Baja": "Álava",
        "Erribera Beitia": "Álava",
        "Salvatierra/Agurain": "Álava",
        "Salvatierra": "Álava",
        "Agurain": "Álava",
        "Samaniego": "Álava",
        "San Millán/Donemiliaga": "Álava",
        "San Millán": "Álava",
        "Donemiliaga": "Álava",
        "Urkabustaiz": "Álava",
        "Valdegovía/Gaubea": "Álava",
        "Valdegovía": "Álava",
        "Gaubea": "Álava",
        "Villabuena de Álava/Eskuernaga": "Álava",
        "Villabuena de Álava": "Álava",
        "Eskuernaga": "Álava",
        "Vitoria-Gasteiz": "Álava",
        "Vitoria": "Álava",
        "Gasteiz": "Álava",
        "Yécora/Iekora": "Álava",
        "Yécora": "Álava",
        "Iekora": "Álava",
        "Zalduondo": "Álava",
        "Zambrana": "Álava",
        "Zigoitia": "Álava",
        "Zuia": "Álava",

        # Navarra
        "Abáigar": "Navarra",
        "Abárzuza/Abartzuza": "Navarra",
        "Abárzuza": "Navarra",
        "Abartzuza": "Navarra",
        "Abaurregaina/Abaurrea Alta": "Navarra",
        "Abaurregaina": "Navarra",
        "Abaurrea Alta": "Navarra",
        "Abaurrepea/Abaurrea Baja": "Navarra",
        "Abaurrepea": "Navarra",
        "Abaurrea Baja": "Navarra",
        "Aberin": "Navarra",
        "Ablitas": "Navarra",
        "Adiós": "Navarra",
        "Aguilar de Codés": "Navarra",
        "Aibar/Oibar": "Navarra",
        "Aibar": "Navarra",
        "Oibar": "Navarra",
        "Allín/Allin": "Navarra",
        "Allín": "Navarra",
        "Allin": "Navarra",
        "Allo": "Navarra",
        "Altsasu/Alsasua": "Navarra",
        "Altsasu": "Navarra",
        "Alsasua": "Navarra",
        "Améscoa Baja": "Navarra",
        "Ancín/Antzin": "Navarra",
        "Ancín": "Navarra",
        "Antzin": "Navarra",
        "Andosilla": "Navarra",
        "Ansoáin/Antsoain": "Navarra",
        "Ansoáin": "Navarra",
        "Antsoain": "Navarra",
        "Anue": "Navarra",
        "Añorbe": "Navarra",
        "Aoiz/Agoitz": "Navarra",
        "Aoiz": "Navarra",
        "Agoitz": "Navarra",
        "Araitz": "Navarra",
        "Arakil": "Navarra",
        "Aranarache/Aranaratxe": "Navarra",
        "Aranarache": "Navarra",
        "Aranaratxe": "Navarra",
        "Arano": "Navarra",
        "Arantza": "Navarra",
        "Aras": "Navarra",
        "Arbizu": "Navarra",
        "Arce/Artzi": "Navarra",
        "Arce": "Navarra",
        "Artzi": "Navarra",
        "Aria": "Navarra",
        "Aribe": "Navarra",
        "Armañanzas": "Navarra",
        "Arróniz": "Navarra",
        "Arruazu": "Navarra",
        "Artajona": "Navarra",
        "Artazu": "Navarra",
        "Atez/Atetz": "Navarra",
        "Atez": "Navarra",
        "Atetz": "Navarra",
        "Auritz/Burguete": "Navarra",
        "Auritz": "Navarra",
        "Burguete": "Navarra",
        "Ayegui/Aiegi": "Navarra",
        "Ayegui": "Navarra",
        "Aiegi": "Navarra",
        "Azagra": "Navarra",
        "Azuelo": "Navarra",
        "Bakaiku": "Navarra",
        "Barañain": "Navarra",
        "Barásoain": "Navarra",
        "Barbarin": "Navarra",
        "Bargota": "Navarra",
        "Barillas": "Navarra",
        "Basaburua": "Navarra",
        "Baztan": "Navarra",
        "Beintza-Labaien": "Navarra",
        "Beintza": "Navarra",
        "Labaien": "Navarra",
        "Beire": "Navarra",
        "Belascoáin": "Navarra",
        "Bera": "Navarra",
        "Berbinzana": "Navarra",
        "Beriáin": "Navarra",
        "Berrioplano": "Navarra",
        "Berriozar": "Navarra",
        "Bertizarana": "Navarra",
        "Betelu": "Navarra",
        "Bidaurreta": "Navarra",
        "Biurrun-Olcoz": "Navarra",
        "Biurrun": "Navarra",
        "Olcoz": "Navarra",
        "Buñuel": "Navarra",
        "Burgui/Burgi": "Navarra",
        "Burgui": "Navarra",
        "Burgi": "Navarra",
        "Burlada/Burlata": "Navarra",
        "Burlada": "Navarra",
        "Burlata": "Navarra",
        "Cabanillas": "Navarra",
        "Cabredo": "Navarra",
        "Cadreita": "Navarra",
        "Caparroso": "Navarra",
        "Cárcar": "Navarra",
        "Carcastillo": "Navarra",
        "Cascante": "Navarra",
        "Cáseda": "Navarra",
        "Castejón": "Navarra",
        "Castillonuevo": "Navarra",
        "Cendea de Olza/Oltza Zendea": "Navarra",
        "Cendea de Olza": "Navarra",
        "Oltza Zendea": "Navarra",
        "Cendea de Cizur": "Navarra",
        "Cizur Mayor": "Navarra",
        "Corella": "Navarra",
        "Cortes": "Navarra",
        "Desojo": "Navarra",
        "Dicastillo": "Navarra",
        "Donamaria": "Navarra",
        "Doneztebe/Santesteban": "Navarra",
        "Doneztebe": "Navarra",
        "Santesteban": "Navarra",
        "Echarri": "Navarra",
        "El Busto": "Navarra",
        "Elgorriaga": "Navarra",
        "Enériz/Eneritz": "Navarra",
        "Enériz": "Navarra",
        "Eneritz": "Navarra",
        "Eratsun": "Navarra",
        "Ergoiena": "Navarra",
        "Erro": "Navarra",
        "Eslava": "Navarra",
        "Esparza de Salazar/Espartza Zaraitzu": "Navarra",
        "Esparza de Salazar": "Navarra",
        "Espartza Zaraitzu": "Navarra",
        "Espronceda": "Navarra",
        "Estella-Lizarra": "Navarra",
        "Estella": "Navarra",
        "Lizarra": "Navarra",
        "Esteribar": "Navarra",
        "Etayo": "Navarra",
        "Etxalar": "Navarra",
        "Etxarri Aranatz": "Navarra",
        "Etxauri": "Navarra",
        "Eulate": "Navarra",
        "Ezcabarte": "Navarra",
        "Ezcároz/Ezkaroze": "Navarra",
        "Ezcároz": "Navarra",
        "Ezkaroze": "Navarra",
        "Ezkurra": "Navarra",
        "Ezprogui": "Navarra",
        "Falces": "Navarra",
        "Fitero": "Navarra",
        "Fontellas": "Navarra",
        "Funes": "Navarra",
        "Fustiñana": "Navarra",
        "Galar": "Navarra",
        "Gallipienzo/Galipentzu": "Navarra",
        "Gallipienzo": "Navarra",
        "Galipentzu": "Navarra",
        "Gallués/Galoze": "Navarra",
        "Gallués": "Navarra",
        "Galoze": "Navarra",
        "Garaioa": "Navarra",
        "Garde": "Navarra",
        "Garínoain": "Navarra",
        "Garralda": "Navarra",
        "Genevilla": "Navarra",
        "Goizueta": "Navarra",
        "Goñi": "Navarra",
        "Güesa/Gorza": "Navarra",
        "Güesa": "Navarra",
        "Gorza": "Navarra",
        "Guesálaz/Gesalatz": "Navarra",
        "Guesálaz": "Navarra",
        "Gesalatz": "Navarra",
        "Guirguillano": "Navarra",
        "Hiriberri/Villanueva de Aezkoa": "Navarra",
        "Hiriberri": "Navarra",
        "Villanueva de Aezkoa": "Navarra",
        "Huarte/Uharte": "Navarra",
        "Huarte": "Navarra",
        "Uharte": "Navarra",
        "Ibargoiti": "Navarra",
        "Igantzi": "Navarra",
        "Igúzquiza": "Navarra",
        "Imotz": "Navarra",
        "Irañeta": "Navarra",
        "Irurtzun": "Navarra",
        "Isaba/Izaba": "Navarra",
        "Isaba": "Navarra",
        "Izaba": "Navarra",
        "Ituren": "Navarra",
        "Iturmendi": "Navarra",
        "Iza/Itza": "Navarra",
        "Iza": "Navarra",
        "Itza": "Navarra",
        "Izagaondoa": "Navarra",
        "Jaurrieta": "Navarra",
        "Javier": "Navarra",
        "Juslapeña": "Navarra",
        "Lakuntza": "Navarra",
        "Lana": "Navarra",
        "Lantz": "Navarra",
        "Lapoblación": "Navarra",
        "Larraga": "Navarra",
        "Larraona": "Navarra",
        "Larraun": "Navarra",
        "Lazagurría": "Navarra",
        "Leache/Leatxe": "Navarra",
        "Leache": "Navarra",
        "Leatxe": "Navarra",
        "Legarda": "Navarra",
        "Legaria": "Navarra",
        "Leitza": "Navarra",
        "Lekunberri": "Navarra",
        "Leoz/Leotz": "Navarra",
        "Leintz Gatzaga": "Navarra",
        "Leoz": "Navarra",
        "Leotz": "Navarra",
        "Lerga": "Navarra",
        "Lerín": "Navarra",
        "Lesaka": "Navarra",
        "Lezáun": "Navarra",
        "Liédena": "Navarra",
        "Lizoáin/Arriasgoiti": "Navarra",
        "Lizoáin": "Navarra",
        "Arriasgoiti": "Navarra",
        "Lodosa": "Navarra",
        "Lónguida/Longida": "Navarra",
        "Lónguida": "Navarra",
        "Longida": "Navarra",
        "Lumbier": "Navarra",
        "Luquin": "Navarra",
        "Luzaide/Valcarlos": "Navarra",
        "Luzaide": "Navarra",
        "Valcarlos": "Navarra",
        "Mañeru": "Navarra",
        "Marañón": "Navarra",
        "Marcilla": "Navarra",
        "Mélida": "Navarra",
        "Mendavia": "Navarra",
        "Mendaza": "Navarra",
        "Mendigorría": "Navarra",
        "Metauten": "Navarra",
        "Milagro": "Navarra",
        "Mirafuentes": "Navarra",
        "Miranda de Arga": "Navarra",
        "Monreal/Elo": "Navarra",
        "Monreal": "Navarra",
        "Elo": "Navarra",
        "Monteagudo": "Navarra",
        "Morentin": "Navarra",
        "Mues": "Navarra",
        "Murchante": "Navarra",
        "Murieta": "Navarra",
        "Murillo el Cuende": "Navarra",
        "Murillo el Fruto": "Navarra",
        "Muruzábal": "Navarra",
        "Navascués/Nabaskoze": "Navarra",
        "Navascués": "Navarra",
        "Nabaskoze": "Navarra",
        "Nazar": "Navarra",
        "Noáin (Valle de Elorz)/Noain (Elortzibar)": "Navarra",
        "Noáin (Valle de Elorz)": "Navarra",
        "Noain (Elortzibar)": "Navarra",
        "Obanos": "Navarra",
        "Ochagavía/Otsagabia": "Navarra",
        "Ochagavía": "Navarra",
        "Otsagabia": "Navarra",
        "Oco": "Navarra",
        "Odieta": "Navarra",
        "Oitz": "Navarra",
        "Olaibar": "Navarra",
        "Olazti/Olazagutía": "Navarra",
        "Olazti": "Navarra",
        "Olazagutía": "Navarra",
        "Olejua": "Navarra",
        "Olite/Erriberri": "Navarra",
        "Olite": "Navarra",
        "Erriberri": "Navarra",
        "Olóriz/Oloritz": "Navarra",
        "Olóriz": "Navarra",
        "Oloritz": "Navarra",
        "Orbaizeta": "Navarra",
        "Orbara": "Navarra",
        "Orísoain": "Navarra",
        "Orkoien": "Navarra",
        "Oronz/Orontze": "Navarra",
        "Oronz": "Navarra",
        "Orontze": "Navarra",
        "Oroz-Betelu/Orotz-Betelu": "Navarra",
        "Oroz-Betelu": "Navarra",
        "Orotz-Betelu": "Navarra",
        "Orreaga/Roncesvalles": "Navarra",
        "Orreaga": "Navarra",
        "Roncesvalles": "Navarra",
        "Oteiza": "Navarra",
        "Pamplona/Iruña": "Navarra",
        "Pamplona": "Navarra",
        "Iruña": "Navarra",
        "Peralta/Azkoien": "Navarra",
        "Peralta": "Navarra",
        "Azkoien": "Navarra",
        "Petilla de Aragón": "Navarra",
        "Piedramillera": "Navarra",
        "Pitillas": "Navarra",
        "Puente la Reina/Gares": "Navarra",
        "Puente la Reina": "Navarra",
        "Gares": "Navarra",
        "Pueyo": "Navarra",
        "Ribaforada": "Navarra",
        "Romanzado": "Navarra",
        "Roncal/Erronkari": "Navarra",
        "Roncal": "Navarra",
        "Erronkari": "Navarra",
        "Sada": "Navarra",
        "Saldías": "Navarra",
        "Salinas de Oro/Jaitz": "Navarra",
        "Salinas de Oro": "Navarra",
        "Jaitz": "Navarra",
        "San Adrián": "Navarra",
        "San Martín de Unx": "Navarra",
        "Sangüesa/Zangoza": "Navarra",
        "Sangüesa": "Navarra",
        "Zangoza": "Navarra",
        "Sansol": "Navarra",
        "Santacara": "Navarra",
        "Sarriés/Sartze": "Navarra",
        "Sarriés": "Navarra",
        "Sartze": "Navarra",
        "Sartaguda": "Navarra",
        "Sesma": "Navarra",
        "Sorlada": "Navarra",
        "Sunbilla": "Navarra",
        "Tafalla": "Navarra",
        "Tiebas-Muruarte de Reta": "Navarra",
        "Tiebas": "Navarra",
        "Muruarte de Reta": "Navarra",
        "Tirapu": "Navarra",
        "Torralba del Río": "Navarra",
        "Torres del Río": "Navarra",
        "Tudela": "Navarra",
        "Tulebras": "Navarra",
        "Ucar": "Navarra",
        "Uharte-Arakil": "Navarra",
        "Ujué/Uxue": "Navarra",
        "Ujué": "Navarra",
        "Uxue": "Navarra",
        "Ultzama": "Navarra",
        "Unciti": "Navarra",
        "Unzué/Untzue": "Navarra",
        "Unzué": "Navarra",
        "Untzue": "Navarra",
        "Urdazubi/Urdax": "Navarra",
        "Urdazubi": "Navarra",
        "Urdax": "Navarra",
        "Urdiain": "Navarra",
        "Urraul Alto": "Navarra",
        "Urraul Bajo": "Navarra",
        "Urrotz": "Navarra",
        "Urroz-Villa": "Navarra",
        "Urzainqui/Urzainki": "Navarra",
        "Urzainqui": "Navarra",
        "Urzainki": "Navarra",
        "Uterga": "Navarra",
        "Uztárroz/Uztarroze": "Navarra",
        "Uztárroz": "Navarra",
        "Uztarroze": "Navarra",
        "Valle de Egüés/Eguesibar": "Navarra",
        "Valle de Egüés": "Navarra",
        "Eguesibar": "Navarra",
        "Valle de Yerri/Deierri": "Navarra",
        "Valle de Yerri": "Navarra",
        "Deierri": "Navarra",
        "Valtierra": "Navarra",
        "Viana": "Navarra",
        "Vidángoz/Bitankoze": "Navarra",
        "Vidángoz": "Navarra",
        "Bitankoze": "Navarra",
        "Villafranca": "Navarra",
        "Villamayor de Monjardín": "Navarra",
        "Villatuerta": "Navarra",
        "Villava/Atarrabia": "Navarra",
        "Villava": "Navarra",
        "Atarrabia": "Navarra",
        "Yesa": "Navarra",
        "Zabalza/Zabaltza": "Navarra",
        "Zabalza": "Navarra",
        "Zabaltza": "Navarra",
        "Ziordia": "Navarra",
        "Zizur Mayor/Zizur Nagusia": "Navarra",
        "Zizur Mayor": "Navarra",
        "Zizur Nagusia": "Navarra",
        "Zubieta": "Navarra",
        "Zugarramurdi": "Navarra",
        "Zúñiga": "Navarra",
        
        #Otros
        "Santander":"Cantabria"
    }
    
    return mapa_provincias.get(poblacion, "Provincia desconocida")
