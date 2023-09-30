def test_pagina_prediccion(cliente):

	data={"texto":"this is good"}

	respuesta=cliente.post("/prediccion", json=data)

	contenido=respuesta.json()

	assert respuesta.status_code==200
	assert "resultado" in contenido