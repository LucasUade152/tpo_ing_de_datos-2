import pandas as pd
import file 

def exportar_consultas_a_csv():
    # 1. Productos con precio mayor a $100
    productos_caros = list(file.coleccion.find({"precio": {"$gt": 100}}))
    df_caros = pd.DataFrame(productos_caros)
    df_caros.to_csv("productos_caros.csv", index=False)

    # 2. Cantidad de productos por categoría
    conteo_por_categoria = list(file.coleccion.aggregate([
        {"$group": {"_id": "$categoria", "cantidad": {"$sum": 1}}}
    ]))
    df_categoria = pd.DataFrame(conteo_por_categoria)
    df_categoria.rename(columns={"_id": "categoria"}, inplace=True)
    df_categoria.to_csv("productos_por_categoria.csv", index=False)

    # 3. Promedio de precio por categoría
    promedio_precio_categoria = list(file.coleccion.aggregate([
        {"$group": {"_id": "$categoria", "precio_promedio": {"$avg": "$precio"}}}
    ]))
    df_promedio = pd.DataFrame(promedio_precio_categoria)
    df_promedio.rename(columns={"_id": "categoria"}, inplace=True)
    df_promedio.to_csv("promedio_precio_por_categoria.csv", index=False)

    # 4. Productos con bajo stock (<=10)
    bajo_stock = list(file.coleccion.find({"stock": {"$lte": 10}}))
    df_bajo_stock = pd.DataFrame(bajo_stock)
    df_bajo_stock.to_csv("productos_bajo_stock.csv", index=False)

    # 5. Cantidad de productos por género
    conteo_genero = list(file.coleccion.aggregate([
        {"$group": {"_id": "$género", "cantidad": {"$sum": 1}}}
    ]))
    df_genero = pd.DataFrame(conteo_genero)
    df_genero.rename(columns={"_id": "genero"}, inplace=True)
    df_genero.to_csv("productos_por_genero.csv", index=False)

    print("Todos los archivos CSV han sido generados.")