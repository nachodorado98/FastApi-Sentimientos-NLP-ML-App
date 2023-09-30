import pickle
import os
from typing import Optional
from sklearn.pipeline import Pipeline

# Funcion para cargar el algoritmo
def cargarAlgoritmo(ruta:str)->Optional[Pipeline]:

    try:

        ruta_algoritmo=os.path.join(ruta, r"algoritmo/pipeline.pkl")

        with open(ruta_algoritmo, "rb") as archivo:

            modelo=pickle.load(archivo)

        return modelo

    except FileNotFoundError as e:

        return None

# Funcion para obtener la prediccion de la diabetes
def obtenerPrediccion(pipeline:Pipeline, texto:str)->str:

    resultado=pipeline.predict([texto])

    return "Positivo" if resultado[0]==1 else "Negativo"