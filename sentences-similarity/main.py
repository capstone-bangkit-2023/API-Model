import os
import httpx
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()
token = os.environ.get("API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-albert-small-v2"
headers = {"Authorization": f"Bearer {token}"}

class TextRequest(BaseModel):
    data: str
    answer: str

async def query(payload):
    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=headers, json=payload)
        return response.json()

async def main(sentence1, sentence2):
    output = await query({
        "inputs": {
            "source_sentence": sentence1,
            "sentences": [
                sentence2
            ]
        },
    })
    return output[0]

@app.get('/')
def hello():
    return ('Hello World!')

@app.post("/predict")
def predict(text_request: TextRequest):
    data, answer = text_request.data, text_request.answer
    result = asyncio.run(main(data,answer))
    return {'result': result}
