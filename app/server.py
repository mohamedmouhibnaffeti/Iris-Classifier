from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load("app/model.joblib")

classnames = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

app.get('/')
def reed_root():
    return {'message': 'Iris model API'}

@app.post("/predict")
def predict(data: dict):
    features = np.array(data['features']).reshape(1, -1)
    predictions = model.predict(features)
    classname = classnames[predictions][0]
    return {'predicted class': classname}