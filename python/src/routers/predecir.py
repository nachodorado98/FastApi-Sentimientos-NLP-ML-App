from fastapi import APIRouter, status
from typing import Dict
import os

from src.modelos.texto import Texto

from src.utilidades.utils import cargarAlgoritmo, obtenerPrediccion

router_predecir=APIRouter(prefix="/prediccion", tags=["Prediccion"])


@router_predecir.post("", status_code=status.HTTP_200_OK, summary="Devuelve los resultados del sentimiento del texto")
async def predecirTexto(texto:Texto)->Dict:

	"""
	Devuelve el resultado tras realizar una prediccion usando el algoritmo.

	## Respuesta

	200 (OK): Si se obtiene el texto correctamente

	- **Resultado**: El resultado de la prediccion del algoritmo (str).
	"""

	ruta=os.path.dirname(os.path.join(os.path.dirname(__file__)))

	algoritmo=cargarAlgoritmo(ruta)

	prediccion=obtenerPrediccion(algoritmo, texto.texto)

	return {"resultado":prediccion}