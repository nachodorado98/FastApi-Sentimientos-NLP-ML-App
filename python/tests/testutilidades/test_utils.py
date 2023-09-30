import os
from sklearn.pipeline import Pipeline

from src.utilidades.utils import cargarAlgoritmo, obtenerPrediccion

def test_cargar_algoritmo_error():

	ruta_relativa=os.path.abspath("..")

	assert cargarAlgoritmo(ruta_relativa) is None

def test_cargar_algoritmo():

	ruta_relativa=os.path.abspath("..")+"/src"

	algoritmo=cargarAlgoritmo(ruta_relativa)

	assert isinstance(algoritmo, Pipeline)

def test_obtener_prediccion():

	algoritmo=cargarAlgoritmo(os.path.abspath("..")+"/src")

	prediccion=obtenerPrediccion(algoritmo, "i am very happy")

	assert prediccion=="Positivo"