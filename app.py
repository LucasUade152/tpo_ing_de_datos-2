from flask import Flask, jsonify
import file

app = Flask(__name__)

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def get_productos():
    try:
        productos = list(file.coleccion.find({}, {"_id": 0}))  # Excluye _id
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": f"No se pudieron obtener los productos: {str(e)}"}), 500

# Ruta para obtener productos con precio mayor a $100
@app.route('/productos/caros', methods=['GET'])
def get_productos_caros():
    try:
        productos = list(file.coleccion.find({"precio": {"$gt": 100}}, {"_id": 0}))
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": f"No se pudieron obtener los productos caros: {str(e)}"}), 500

# Ruta para productos con bajo stock
@app.route('/productos/bajo_stock', methods=['GET'])
def get_productos_bajo_stock():
    try:
        productos = list(file.coleccion.find({"stock": {"$lte": 10}}, {"_id": 0}))
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": f"No se pudieron obtener productos con bajo stock: {str(e)}"}), 500

# Ruta para contar productos por categoría
@app.route('/productos/categorias', methods=['GET'])
def get_cantidad_por_categoria():
    try:
        resultado = list(file.coleccion.aggregate([
            {"$group": {"_id": "$categoria", "cantidad": {"$sum": 1}}}
        ]))
        for r in resultado:
            r['categoria'] = r.pop('_id')
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": f"No se pudo agrupar por categoría: {str(e)}"}), 500

# Ruta para promedio de precios por categoría
@app.route('/productos/promedio_precio', methods=['GET'])
def get_promedio_precio():
    try:
        resultado = list(file.coleccion.aggregate([
            {"$group": {"_id": "$categoria", "precio_promedio": {"$avg": "$precio"}}}
        ]))
        for r in resultado:
            r['categoria'] = r.pop('_id')
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": f"No se pudo calcular el promedio de precios: {str(e)}"}), 500

# Ruta para contar productos por género
@app.route('/productos/generos', methods=['GET'])
def get_cantidad_por_genero():
    try:
        resultado = list(file.coleccion.aggregate([
            {"$group": {"_id": "$género", "cantidad": {"$sum": 1}}}
        ]))
        for r in resultado:
            r['genero'] = r.pop('_id')
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": f"No se pudo agrupar por género: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
