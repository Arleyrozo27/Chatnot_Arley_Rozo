lugares = {
    "muralla": {
        "descripcion": "La Muralla de Cartagena es un conjunto de fortificaciones históricas.",
        "horario": "Visítala entre 5:00 p.m. y 7:00 p.m.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Murallas_de_Cartagena_de_Indias.JPG"
    },
    "castillo san felipe": {
        "descripcion": "El Castillo San Felipe es una imponente fortaleza colonial.",
        "horario": "Ideal entre 8:00 a.m. y 10:00 a.m.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Castillo_San_Felipe_de_Barajas_Cartagena.jpg"
    },
    "ciudad amurallada": {
        "descripcion": "Centro histórico lleno de arquitectura colonial.",
        "horario": "Recórrela entre 4:00 p.m. y 8:00 p.m.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Ciudad_Amurallada_Cartagena.jpg"
    },
    "playa blanca": {
        "descripcion": "Una hermosa playa en la isla Barú.",
        "horario": "Ve entre 9:00 a.m. y 2:00 p.m.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Playa_Blanca_Cartagena.jpg"
    }
}

def responder(mensaje):
    mensaje = mensaje.lower()
    if "sitios" in mensaje or "lugares" in mensaje:
        return "Estos son algunos sitios turísticos de Cartagena: " + ", ".join([lugar.title() for lugar in lugares.keys()])
    for lugar, info in lugares.items():
        if lugar in mensaje:
            return f"<strong>{lugar.title()}</strong><br><img src='{info['imagen']}' style='width:100%;max-height:200px;margin-top:5px;border-radius:8px'><br>{info['descripcion']}<br><em>{info['horario']}</em>"
    return "Solo respondo sobre sitios turísticos de Cartagena, Colombia."