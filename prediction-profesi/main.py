import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Path, Query

import json

datasets = pd.read_csv('data.csv')
model = tf.keras.models.load_model('./something.h5')

with open('./tokenizer.json') as f:
    tokenizer_data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_data)


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
    predicted_class = np.argmax(predict(item.input), axis=1)

    # get the predicted profession
    result = datasets['Profesi'].unique()[predicted_class[0]]
    return {result}
