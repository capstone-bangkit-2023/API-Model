import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from model import model_predict

app = FastAPI()

class TextRequest(BaseModel):
    data: str
    answer: str

data = 'Pantun adalah salah satu jenis puisi lama yang sangat luas dikenal di Asia tenggara. Pantun memiliki sajak ABAB. Dalam bahasa Sunda pantun disebut paparikan dan dalam bahasa Batak, pantun dikenal dengan sebutan umpasa.'
answer = 'Pantun merupakan salah satu jenis puisi lama pada sastra indonesia'

# @app.get('/')
# def starting():
#     return ('Hello World!')

@app.post("/predict")
async def predict(text_request: TextRequest):
    data, answer = text_request.data, text_request.answer
    result = model_predict(data, answer)
    return {'data': result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
