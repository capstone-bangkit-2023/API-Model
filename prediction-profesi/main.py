import numpy as np
import tensorflow as tf
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Path, Query

datasets = pd.read_csv('./Dataset.csv')
app = FastAPI()

class Item(BaseModel):
    input: list

model = tf.keras.models.load_model('./model-profesi.h5')
    
def predict(value):
    value = np.array(value)
    value = value.reshape(1, -1)
    predict = model.predict(value)
    predicted = np.argmax(predict)
    prediction_class = datasets.loc[datasets['Label'] == predicted].iloc[0]
    prediction = prediction_class['Profesi']
    return prediction

@app.get("/")
def home():
    return "Hello World!"

@app.post("/predict")
def add_item(item: Item):
    result = predict(item.input)
    return {result}
