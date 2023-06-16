<br/>
<p align="center">
  <a href="https://github.com/ShaanCoding/ReadME-Generator">
    <img src="https://raw.githubusercontent.com/capstone-bangkit-2023/mobile-app/main/app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Ayo Pintar</h3>

  <p align="center">
    Smart Quiz Platform

# API Model
We create 2 API(s) model for this application, there is sentence Similarity API and Prediction Profesi API, both of them created using FastAPI and deployed on cloud run

# API Documentation
```
https://docs.google.com/document/d/111WUYr6W-JranLW7XzRj0Vhxbm0PTrXQd-cgmBWAN9Q/edit?usp=sharing
```
  
# Build With
1. Fast API
2. Dockerfile
    
## FastAPI
FastAPI is a modern web framework for building RESTful APIs in Python. It was first released in 2018 and has quickly gained popularity among developers due to its ease of use, speed and robustness. FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data.

Documentation: https://fastapi.tiangolo.com

Source Code: https://github.com/tiangolo/fastapi

To run this file, do
```bash
uvicorn main:app
```
or
```bash
uvicorn main:app --reload
```
to automatically restart the kernel everytime there's a change saved inside `main.py`

```bash
// to create a h5 file
model.save('studytips.h5')

//to export a json file
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

tokenizer_json = tokenizer.to_json()
with open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json, ensure_ascii=False))
//
datasets = pd.read_csv('./data.csv')
model = tf.keras.models.load_model('./studytips.h5')
with open('./tokenizer.json') as f:
    tokenizer_data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_data)
```


# sentences-similarity model deployment
```bash
// to create image api model prediction sentences
gcloud builds submit --tag gcr.io/$DEVSHELL_PROJECT_ID/api-model-sentence:0.1
```

💡 Container Image Deploy v1
---
```bash
ID: 5158895c-ab8f-4827-b982-9833f2c75242
CREATE_TIME: 2023-06-12T15:31:57+00:00
DURATION: 50S
SOURCE: gs://capstone-387513_cloudbuild/source/1686583915.537893-c2269f4ca2be4f06bc81968265e6cdc9.tgz
IMAGES: gcr.io/capstone-387513/api-model-sentence:0.1
STATUS: SUCCESS
```


# prediction-profesi model deployment
```bash
// to create image api model prediction profesi
gcloud builds submit --tag [gcr.io/$DEVSHELL_PROJECT_ID/api-model-profesi:0.](http://gcr.io/$DEVSHELL_PROJECT_ID/api-model:0.1)1
```

💡 Container Image Deploy v1
---
```bash
ID: 9823a108-868b-450b-ba1b-6adb4d516a18
CREATE_TIME: 2023-06-14T14:22:19+00:00
DURATION: 6M13S
SOURCE: gs://capstone-387513_cloudbuild/source/1686752536.554975-01c993260cb94f238c0dce820dbda788.tgz
IMAGES: gcr.io/capstone-387513/api-model-profesi:0.1
STATUS: SUCCESS
```
