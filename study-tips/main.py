import numpy as np
import pandas as pd
import tensorflow as tf
#import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Path, Query

import json

datasets = pd.read_csv('./data.csv')
model = tf.keras.models.load_model('./studytips.h5')

with open('./tokenizer.json') as f:
    tokenizer_data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_data)


def predict(input):
    predict_sequence = tokenizer.texts_to_sequences([input])
    predict_padded = pad_sequences(predict_sequence, maxlen=2, padding='post')
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
    result = datasets['Study Tips'].unique()[predicted_class[0]]
    return {result}
