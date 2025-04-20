# TPO Ingeniería de Datos II

Este proyecto corresponde al Trabajo Práctico Obligatorio (TPO) de la materia **Ingeniería de Datos II** de la Universidad Argentina de la Empresa (UADE). El objetivo principal es aplicar los conocimientos adquiridos sobre bases de datos NoSQL, específicamente MongoDB, en conjunto con Python para la gestión y análisis de datos.

## 🧩 Contenido del Proyecto

- **`TiendaRopa.json`**: Dataset principal que contiene información sobre productos de una tienda de ropa.
- **`app.py`**, **`main.py`**, **`generador.py`**, **`exportador.py`**, **`file.py`**: Scripts en Python que permiten realizar operaciones CRUD en MongoDB, generar datos, exportar resultados y manejar archivos.
- **Archivos CSV**: Resultados de consultas y análisis realizados sobre los datos, como productos por categoría, productos caros, productos con bajo stock, entre otros.

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **MongoDB**: Base de datos NoSQL utilizada para almacenar y gestionar la información.
- **PyMongo**: Librería de Python para interactuar con MongoDB.
- **Pandas**: Librería para análisis y manipulación de datos.
- **CSV**: Formato de archivo para exportar los resultados de las consultas.
- **FLASK**: Libreria para hacer API

## 🚀 Instrucciones para Ejecutar el Proyecto

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/LucasUade152/tpo_ing_de_datos-2.git
   cd tpo_ing_de_datos-2
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv entorno
   source entorno/bin/activate  # En Windows: entorno\Scripts\activate
   ```

3. **Instalar las dependencias necesarias:**

   ```bash
   pip install pymongo pandas flask
   ```

4. **Configurar la conexión a MongoDB:**

   Asegurate de tener una instancia de MongoDB en funcionamiento. Si es local, la conexión por defecto suele ser `mongodb://localhost:27017/`. Si utilizás una instancia en la nube, como MongoDB Atlas, reemplazá la URI en los scripts correspondientes.

5. **Ejecutar los scripts:**

   - Para cargar datos: `python generador.py`
   - Para realizar consultas y exportar resultados: `python main.py` o `python exportador.py`
   - Para arrancar la API: `python app.py`

## 📁 Estructura del Proyecto

```
tpo_ing_de_datos-2/
├── TiendaRopa.json
├── app.py
├── main.py
├── generador.py
├── exportador.py
├── file.py
├── productos_bajo_stock.csv
├── productos_caros.csv
├── productos_por_categoria.csv
├── productos_por_genero.csv
├── promedio_precio_por_categoria.csv
└── .gitignore
```

## 👥 Autores

- Facundo Pérez Espinosa 
- Kevin Villalba 
- Sebastián Lin 
- Octavio Mansi 
- Santiago Rafael Guerra  
- Lucas Ezequiel Cascardo 



