from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import sqlite3
import pickle
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import uvicorn


# Cargar el modelo de machine learning
MODEL_PATH = "./data/advertising_model.pkl"
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)


# Configuración de la base de datos
df = pd.read_csv('./data/advertising_clean.csv', index_col=[0])
conn = sqlite3.connect('Adv_data.db')
df.to_sql('Advertising', conn, if_exists='replace', index=False)

app = FastAPI()

conec = sqlite3.connect('Adv_data.db')
cursor = conec.cursor()


# Bienvenida
@app.get("/")
async def saludo():
    return "Hola, bienvenido a la app de predicción de costes"


# 1. Endpoint de predicción
@app.get("/predict")
async def prediccion(TV: int, radio: int, newpaper: int):
    data_inversion = {'TV': TV, 'radio': radio, 'newpaper': newpaper}
    input = pd.DataFrame([data_inversion])
    prediction = model.predict(input)
    return {"Prediction": prediction[0]}


# 2. Endpoint de ingesta de datos
@app.post("/add_data")
async def add_data(TV,radio, newpaper, sales):
        cursor.execute('''INSERT INTO Advertising (TV, radio, newpaper, sales) 
                        VALUES (?,?,?,?)''', (TV,radio,newpaper,sales))
        conn.commit()
        return "Datos Ingresados Correctamente"


# 3. Endpoint de reentramiento del modelo
@app.post("/retrain")
async def retrain():
    
        df = pd.read_sql_query("SELECT * FROM Advertising", conn)
    
        X = df[['TV', 'radio', 'newpaper']]  
        y = df['sales']  
        
        model.fit(X, y)
        with open(MODEL_PATH, 'wb') as model_file:
            pickle.dump(model, model_file)
        
        return 'Modelo Entrenado Correctamente'


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)