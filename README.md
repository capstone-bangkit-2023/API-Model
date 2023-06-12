# FastAPI

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
IMAGES: [gcr.io/capstone-387513/api-model-sentence:0.1](http://gcr.io/capstone-387513/api-model-sentence:0.1)
STATUS: SUCCESS
```


# prediction-profesi model deployment
```bash
// to create image api model prediction profesi
gcloud builds submit --tag [gcr.io/$DEVSHELL_PROJECT_ID/api-model:0.1](http://gcr.io/$DEVSHELL_PROJECT_ID/api-model:0.1)
```

💡 Container Image Deploy v1
---
```bash
ID: f9ae2c21-7bed-427e-a525-761728f740e9
CREATE_TIME: 2023-06-06T06:59:21+00:00
DURATION: 6M29S
SOURCE: gs://capstone-387513_cloudbuild/source/1686034757.32025-db57ba326a104752bce8cbede304be71.tgz
IMAGES: [gcr.io/capstone-387513/api-model:0.1](http://gcr.io/capstone-387513/api-model:0.1)
STATUS: SUCCESS
```

# study-tips model deployment
```bash
// to create image api model prediction study tips
gcloud builds submit --tag [gcr.io/$DEVSHELL_PROJECT_ID/api-model-study-tips:0.1](http://gcr.io/$DEVSHELL_PROJECT_ID/api-model:0.1)
```

💡 Container Image Deploy v1
---
```bash
ID: ffd874e7-b171-432a-9372-3ffdc5bf83aa
CREATE_TIME: 2023-06-06T07:28:04+00:00
DURATION: 6M42S
SOURCE: gs://capstone-387513_cloudbuild/source/1686036481.405515-97622569f88e4f2f863bc72492d2e142.tgz
IMAGES: [gcr.io/capstone-387513/api-model-study-tips:0.1](http://gcr.io/capstone-387513/api-model-study-tips:0.1)
STATUS: SUCCESS
```
