import json
import generador
import file
import exportador

# Generar productos y guardarlos en JSON
generador.generar_productos_json(10, "TiendaRopa.json")
print("Se han generado los productos y se han guardado en el archivo TiendaRopa.json.")

# Leer los productos generados
with open('TiendaRopa.json', 'r') as json_file:
    data = json.load(json_file)

# Insertar en la base de datos
try:
    resultado = file.coleccion.insert_many(data)
    print(f"Se han insertado {len(resultado.inserted_ids)} productos en la base de datos.")
except Exception as e:
    print("Error al insertar los productos:", e)

# CONSULTAS EN CONSOLA
print("\nEjecutando consultas en consola...")

productos_caros = file.coleccion.find({"precio": {"$gt": 100}})
print("\nProductos con precio mayor a $100:")
for producto in productos_caros:
    print(producto)

conteo_por_categoria = file.coleccion.aggregate([
    {"$group": {"_id": "$categoria", "cantidad": {"$sum": 1}}}
])
print("\nCantidad de productos por categoría:")
for categoria in conteo_por_categoria:
    print(f"{categoria['_id']}: {categoria['cantidad']}")

promedio_precio_categoria = file.coleccion.aggregate([
    {"$group": {"_id": "$categoria", "precio_promedio": {"$avg": "$precio"}}}
])
print("\nPromedio de precio por categoría:")
for categoria in promedio_precio_categoria:
    print(f"{categoria['_id']}: ${round(categoria['precio_promedio'], 2)}")

bajo_stock = file.coleccion.find({"stock": {"$lte": 10}})
print("\nProductos con bajo stock (<= 10 unidades):")
for producto in bajo_stock:
    print(producto)

conteo_genero = file.coleccion.aggregate([
    {"$group": {"_id": "$género", "cantidad": {"$sum": 1}}}
])
print("\nCantidad de productos por género:")
for genero in conteo_genero:
    print(f"{genero['_id']}: {genero['cantidad']}")

# Exportar resultados a CSV
print("\nExportando datos a archivos CSV...")
exportador.exportar_consultas_a_csv()

# Cerrar la conexión a MongoDB
file.MONGO_URI.close()
