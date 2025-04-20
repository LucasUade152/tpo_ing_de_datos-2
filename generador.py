import json
import random

def generar_productos_json(cantidad_productos, nombre_archivo="TiendaRopa.json"):
    # Diccionario que asocia descripciones con categorías
    productos_dict = {
        "Remera deportiva": "Camisas",
        "Camisa de vestir": "Camisas",
        "Pantalón de jean": "Pantalones",
        "Pantalón deportivo": "Pantalones",
        "Zapatillas urbanas": "Zapatos",
        "Zapatos de cuero": "Zapatos",
        "Gorra ajustable": "Accesorios",
        "Bufanda de lana": "Accesorios",
        "Chaqueta impermeable": "Abrigos",
        "Vestido de verano": "Vetidos",
        "Sweater de algodón": "Abrigos",
        "Falda plisada": "Pantalones",
        "Buzo con capucha": "Abrigos",
        "Shorts de playa": "Pantalones",
        "Campera térmica": "Abrigos",
        "Guantes de invierno": "Accesorios"
    }

    generos = ["Masculino", "Femenino", "Unisex"]
    talles = ["S", "M", "L", "XL"]
    colores = ["Rojo", "Azul", "Verde", "Negro", "Blanco","Violeta", "Amarillo", "Gris"]
    telas = ["Algodón", "Poliéster", "Lana", "Lino", "Friza"]
    destinatarios = ["Adulto", "Infantil", "Adolescente"]

    productos = []

    for i in range(1, cantidad_productos + 1):
        descripcion = random.choice(list(productos_dict.keys()))
        categoria = productos_dict[descripcion]  # Asignar la categoría correspondiente

        producto = {
            "_id": i,
            "descripcion": descripcion,
            "categoria": categoria,
            "género": random.choice(generos),
            "talle": random.choice(talles),
            "color": random.choice(colores),
            "tela": random.choice(telas),
            "destinatario": random.choice(destinatarios),
            "precio": round(random.uniform(10, 500), 2),
            "stock": random.randint(1, 100)
        }
        productos.append(producto)

    with open(nombre_archivo, "w") as file:
        json.dump(productos, file, indent=4)

    print(f"Archivo '{nombre_archivo}' generado con éxito con {cantidad_productos} productos.")