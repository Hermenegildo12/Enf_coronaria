import pandas as pd
import numpy as np
import re
import requests
import matplotlib as plt
from collections import Counter
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from funciones import *
os.getcwd()

datos=pd.read_csv("../input/heart.csv",encoding="ISO-8859-1")
# print(datos.columns)
datos.head()
datos.dtypes
datos.shape
datos.isnull().sum()
datos.columns = datos.columns.map(lambda x: x.strip().lower().replace(" ",""))
datos.columns
datos.columns=["edad","sexo","dolor_pecho","presion_reposo","colesterol","glucemia_ayuna",
              "ecg_reposo","frec_card_max","angina_ind_ejer","descn_st_tras_ejer","pend_st_en ejer",
              "vasos_fluoros","reversibilidad","enf"]
lista=[e for e in range(303)]
datos["id"]=lista
datos["enf"].value_counts()
edad=datos["edad"].describe()
datos[datos["edad"]==29]
presion=datos["presion_reposo"].describe()
colesterol=datos["colesterol"].describe()
frecue=datos["frec_card_max"].describe()
datos.columns
datos.head()
datos.shape
    
datos["presion_reposo2"] = datos["presion_reposo"].apply(rango)


#Saco una Api con Token pero al final no la voy a usar.
#La dejo porque el ejercicio va de esto.
""""""""""""""""
load_dotenv(dotenv_path='.env')
token = os.getenv('token', 'No value found')
def peticion (url, params={}):
   headers = {
      "api_key": "token {}".format(token)
   }
   response = requests.get(url,headers=headers, params=params)
   print(response.status_code)
   return response.json()

url = 'https://api.fda.gov/drug/event.json?api_key='
params=params
dat=peticion(url,params)

dat.keys()
for e in dat["results"]:
    print(e)
"""""""""""
url="https://cima.aemps.es/cima/dochtml/ft/77542/FichaTecnica_77542.html"
rese=requests.get(url)
diu=rese.text
diure=BeautifulSoup(diu,"html.parser")
medicamen=diure.select("#content > div > div.col-sm-9 > section:nth-child(3) > div > p > span")
type(diure)
a=diure.text
farmacos=[re.search("HIDROCLOROTIAZIDA",a).group().lower()]
farmacos
#Las tablas de farmacos que he encontrado son en pdf por ello he ido a un unico farmaco
#deberia ir haciendo esto a cada farmaco de hipertension arterial pero como no me da tiempo
#el resto los voy a crear yo.
listo=0
datos["farmacos"]=listo
datos.columns
datos["presion_reposo2"].value_counts()
g = [e for e in datos["presion_reposo2"]]
far = []
for i in range(len(g)):
    if g[i] == "Óptimo":
        far.append("No necesario")
    elif g[i]=="Normal":
        far.append("No necesario")
    elif g[i]=="ligeramente elevada":
        far.append("0")
    elif g[i]=="HTA Grado 1":
        far.append("1")
    elif g[i]=="HTA Grado 2":
        far.append("2")
    elif g[i]=="HTA Grado 3":
        far.append("3")
datos['farmacos'] = far

farmaco_dato={"0" :'medidas_dieteticas',
                '1' : "diureticos",
                 "2":"b_bloqueante",
                 "3":"a_b_bloqueate",
                 "4":"IECA",
                  "5":"ARA"}

ver=datos[(datos["ecg_reposo"]==1) & (datos["descn_st_tras_ejer"]>=1.0)&
          (datos["pend_st_en ejer"]==1) | (datos["pend_st_en ejer"]==3)]
sin=ver["enf"].value_counts()

#Apesar de tener los registros de ecg alterados, la mayoria no presentan "enfermedad", porque esta se considera 
#en torno a un estrechamiento de >50% del diametro de la arteria coronaria principal.
sen=ver["dolor_pecho"].value_counts()



#Sin embargo la mayoria si que presentan sintomas de tipo anginoso.

def farmacos (e):
    farmaco_dato={0 :'medidas_dieteticas',
    1 : "diureticos",
    2:"b_bloqueante",
    3:"a_b_bloqueate",
    4:"IECA",
    5:"ARA"}
    return farmaco_dato[e]


def presion_farmaco(ID): 
    farmaco_dato={0 :'medidas_dieteticas',
    1 : "diureticos",
    2:"b_bloqueante",
    3:"a_b_bloqueate",
    4:"IECA",
    5:"ARA"}
    id_presion = pd.DataFrame(datos, columns=['id','presion_reposo2','farmacos'])
    id_presion = id_presion[id_presion['id']==int(ID)]
    id_presion["farmacos"]=faramaco_dato[]
    return id_presion


# Grafico que evalua el descenso del segmento ST durante una ergonometría (Prueba positiva >1mm). 
#Se observa como hay mas casos de pruebas positivas en los grupos de presión arterial normal o Grado 1.
#Ya que con esta prueba se quiere descartar una angina estable, la cual solo se manifiesta al someter a mayor
#demanda el corazón. Lo que indicaría que con HTA de grados superiores, no sería necesaria por su relación estrecha con 
#la patologia cardiaca. A lo que de realizarla se ve como ese segmeto desciende en mayor medida, indicando isquemia
#subendocardica.

""""ya= datos["descn_st_tras_ejer"]
x= datos["presion_reposo2"]

p= figure(
   tools="pan,box_zoom,reset,save",
   y_range=[6.5,0.0],x_range=["óptimo","Normal","ligeramente elevada","HTA Grado 1","HTA Grado 2","HTA Grado 3"],
   x_axis_label='Grados presion arterial', y_axis_label='descenso segmento ST'
)

p.circle(x,ya, legend="descn_st_tras_ejer", fill_color="black", size=10)

show(p,new="tab")

# Grafico comparando el colesterol y la presión arterial según la edad.
y1= datos["colesterol"]
ya= datos["presion_reposo"]
x= datos["edad"]


p= figure(tools="pan,box_zoom,reset,save",y_range=[100,500], x_range=[25,90],x_axis_label='edad', y_axis_label='concentracion')

p.circle(x,y1, legend="colesterol",fill_color="red", size=10)
p.circle(x,ya, legend="presion_reposo", fill_color="black", size=10)


show(p,new="tab")"""