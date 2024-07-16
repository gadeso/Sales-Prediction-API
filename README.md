# Sales Prediction API

Este repositorio contiene una API para predecir ventas utilizando un modelo de machine learning. 

La API está implementada en Python y utiliza FastAPI para manejar las solicitudes HTTP. 

El archivo principal del proyecto se encuentra en la carpeta `ejercicios` y se llama `app_model.py`.

- **ejercicios/**: Contiene el código principal de la API y el modelo entrenado.
- **data/**: Contiene los conjuntos de datos utilizados para entrenar y probar el modelo.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
- **README.md**: Este archivo que estás leyendo.


#### Ejecuta la aplicación a través de Bash:
python app_model.py
La API estará disponible en http://127.0.0.1:5000


## Endpoints de la API

- 1. Predicción de Ventas
URL: /predict
Método: POST
Datos de Entrada: TV, radio y newpaper.
Ejemplo de Solicitud
{
  "TV": 230.1,
  "radio": 37.8,
  "newpaper": 69.2
}

- 2. Añadir Datos
URL: /add_data
Método: POST
Datos de Entrada: TV, radio, newpaper y sales.
Ejemplo de Solicitud
{
  "TV": 44.5,
  "radio": 39.3,
  "newpaper": 45.1,
  "sales": 10.5
}

- 3. Reentrenar el Modelo
URL: /retrain
Método: POST
Datos de Entrada: Ninguno.
