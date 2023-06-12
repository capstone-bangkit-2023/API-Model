import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from model import model_predict

app = FastAPI()

class TextRequest(BaseModel):
    data: str
    answer: str

@app.get('/')
def hello():
    return ('Hello World!')

@app.post("/predict")
def predict(text_request: TextRequest):
    data, answer = text_request.data, text_request.answer
    result = model_predict(data, answer)
    return {'result': result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
