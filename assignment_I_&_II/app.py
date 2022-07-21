from fastapi import FastAPI, Depends, HTTPException, status
from src.model import Model
from src.constants import Constants
from pydantic_model import InputData
import pickle
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.postresql import Postgres
import pandas as pd
import datetime


security = HTTPBasic()

client = FastAPI()
file = open(Constants.model_name,'rb')
model = pickle.load(file)
file.close()
file = open(Constants.scalar_name,'rb')
scalar = pickle.load(file)
file.close()
db = Postgres()


def get_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    df = db.get_data(f"SELECT password FROM credentials WHERE username = '{credentials.username}'")
    if df.empty:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username not registered!",
        )
    if credentials.password != df['password'].values[0]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials!",
        )
    return credentials.username

@client.post("/prediction")
def predict(data: InputData ,username: str = Depends(get_credentials), is_test=bool(False)):
    # delete is_test from data
    
    prediction = Model.make_pred_api(data, model, scalar)
    prediction_df = pd.DataFrame([[data.customer_id, prediction, datetime.datetime.now()]], columns=["customer_id", "prediction", "request_date"])
    if is_test:
        return {"username": username , "prediction_class" : prediction}
    table = Constants.prediction_table + "_api"
    db.insert_api_prediction(table, prediction_df)
    return {"username": username , "prediction_class" : prediction}