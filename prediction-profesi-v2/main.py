import numpy as np
import tensorflow as tf
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Path, Query

datasets = pd.read_csv('Dataset Profesi - Sheet1.csv')
model = tf.keras.models.load_model('./model-profesi.h5')

"""with open('./tokenizer.json') as f:
    tokenizer_data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_data)
"""

def predict(input):
    predict_sequence = tokenizer.texts_to_sequences([input])
    predict_padded = pad_sequences(predict_sequence, maxlen=max_length, padding=pad_typev)
    predictions = model.predict(predict_padded)
    return predictions


app = FastAPI()

class Item(BaseModel):
    input: str

@app.post("/")
def add_item(item: Item):
    # get predicted class
    predicted = np.argmax(predict)
    prediction_class = datasets.loc[datasets['Label'] == predicted].iloc[0]
    

    # get the predicted profession
    prediction = prediction_class['Profesi']
    result = datasets['Profesi'].unique()[prediction_class[0]]
    return {prediction}
